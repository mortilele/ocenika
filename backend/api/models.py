from dateutil.relativedelta import relativedelta
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from utils.models import IntegerRangeField
from utils.file_upload import university_path, professor_path
from utils import constants
from django.db.models import Avg
from django.utils import timezone
from django.conf import settings


class University(models.Model):
    class Meta:
        verbose_name = 'Университет'
        verbose_name_plural = 'Университеты'

    name = models.CharField(max_length=500, verbose_name='Название')
    abbreviation = models.CharField(max_length=500, verbose_name='Аббревиатура', blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Описание')
    logo = models.ImageField(upload_to=university_path, max_length=1000, verbose_name='Лого', null=True,
                             default=constants.NO_IMAGE)
    rating = models.FloatField(default=0,
                               blank=True,
                               null=True,
                               verbose_name='Рейтинг')

    def __str__(self):
        return self.name

    def recalculate_rating(self):
        self.rating = self.professor_set.aggregate(avg=Avg('average_rating'))['avg']
        self.save()

    def save(self, *args, **kwargs):
        if not self.abbreviation:
            if len(self.name.split()) != 1:
                self.abbreviation = "".join(w[0].upper() for w in self.name.split())
            else:
                self.abbreviation = self.name
        super(University, self).save(*args, **kwargs)


class Professor(models.Model):
    class Meta:
        verbose_name = 'Преподователь'
        verbose_name_plural = 'Преподаватели'
        ordering = ['id']

    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    patronymic = models.CharField(default='', blank=True, max_length=50, verbose_name='Отчество')
    full_name = models.CharField(blank=True, null=True, max_length=200, verbose_name='ФИО')
    universities = models.ManyToManyField(University,
                                          verbose_name='Университеты в котором он преподает',
                                          blank=True)
    average_rating = models.PositiveIntegerField(default=0, verbose_name='Средний рейтинг')
    rating_count = models.PositiveIntegerField(default=0, verbose_name='Количество оценок')
    avatar = models.ImageField(upload_to=professor_path, verbose_name='Аватар', null=True, default=constants.NO_AVATAR)

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        self.full_name = '{} {} {}'.format(self.first_name, self.last_name, self.patronymic).strip()
        super(Professor, self).save(*args, **kwargs)

    def recalculate_average_rating(self):
        if self.ratings.exists():
            valid_ratings = self.ratings.filter(created_at__gte=timezone.now() - relativedelta(months=6),
                                                status=constants.ACCEPTED)
            if valid_ratings:
                valued_ratings = valid_ratings.filter(value__gte=1)
                if valued_ratings:
                    self.average_rating = valued_ratings.aggregate(avg=Avg('value'))['avg']
                self.rating_count = valid_ratings.count()
                self.save()
                for university in self.universities.all():
                    university.recalculate_rating()


class Subject(models.Model):
    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    name = models.CharField(max_length=300, verbose_name='Название предмета')
    abbreviation = models.CharField(max_length=300, verbose_name='Аббревиатура', blank=True, null=True)
    professors = models.ManyToManyField(Professor,
                                        related_name='subjects',
                                        verbose_name='Преподаватели этого предмета',
                                        blank=True)
    university = models.ManyToManyField(University,
                                        related_name='subjects',
                                        verbose_name='Университеты',
                                        blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.abbreviation:
            if len(self.name.split()) != 1:
                self.abbreviation = "".join(w[0].upper() for w in self.name.split())
            else:
                self.abbreviation = self.name
        super(Subject, self).save(*args, **kwargs)


class ProfessorReviewManager(models.Manager):

    @staticmethod
    def last_review_in_week(user, professor):
        professor_ratings = ProfessorReview.objects.filter(professor=professor,
                                                           user=user)
        if professor_ratings:
            last_rating = professor_ratings.order_by('-created_at', ).first()
            if (timezone.now() - last_rating.created_at).days < 7:
                return True
        return False


class ProfessorReview(models.Model):
    class Meta:
        verbose_name = 'Отзыв преподавателю'
        verbose_name_plural = 'Отзывы преподавателю'
        ordering = ['-created_at']

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.DO_NOTHING,
                             related_name='professor_reviews',
                             verbose_name='Пользователь')
    review = models.TextField(verbose_name='Отзыв')
    value = models.PositiveSmallIntegerField(default=0,
                                             blank=True,
                                             validators=[
                                                 MinValueValidator(0),
                                                 MaxValueValidator(5)
                                             ],
                                             verbose_name='Оценка')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    professor = models.ForeignKey(Professor,
                                  on_delete=models.CASCADE,
                                  related_name='ratings',
                                  verbose_name='Преподаватель')
    status = models.CharField(verbose_name='Статус',
                              max_length=100,
                              choices=constants.REVIEW_STATUSES,
                              default=constants.ON_MODERATION)
    subject = models.ForeignKey(Subject,
                                on_delete=models.DO_NOTHING,
                                blank=True,
                                null=True,
                                verbose_name='Предмет')
    moderator_message = models.CharField(max_length=500,
                                         default='',
                                         verbose_name='Сообщение от системы')
    decline_reason = models.CharField(default=constants.NO_REASON,
                                      choices=constants.REVIEW_DECLINE_REASONS,
                                      max_length=500,
                                      verbose_name='Причина отказа')
    custom_decline_reason = models.CharField(blank=True,
                                             null=True,
                                             max_length=5000,
                                             verbose_name='Комментарий причины отказа от модератора')
    objects = ProfessorReviewManager()

    def save(self, *args, **kwargs):
        super(ProfessorReview, self).save(*args, **kwargs)
        self.professor.recalculate_average_rating()

    def __str__(self):
        return f'{self.professor} {self.status}'


class RatingApplication(models.Model):
    class Meta:
        verbose_name = 'Заявка на действительность отзыва'
        verbose_name_plural = 'Заявки на действильность отзыва'

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='applications')
    review = models.OneToOneField(ProfessorReview,
                                  on_delete=models.CASCADE,
                                  related_name='application')
    user_proof_data = models.TextField(verbose_name='Текстовое доказательство',
                                       blank=True)
    user_proof_file = models.FileField(verbose_name='Файловое доказательство',
                                       blank=True)
    is_viewed = models.BooleanField(default=False,
                                    verbose_name='Рассмотрен?')

    def __str__(self):
        return f'{self.user} {self.review}'


class PrivacyPolicy(models.Model):
    file = models.FileField(verbose_name='Документ')

    class Meta:
        verbose_name = 'Политика конфиденциальности'
