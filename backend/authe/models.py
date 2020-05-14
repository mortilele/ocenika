from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import ugettext_lazy as _
from django.template.loader import render_to_string

from rest_framework.authtoken.models import Token

from utils.email_worker import EmailThread
from .managers import UserManager

from utils.file_upload import transcript_path
from api.models import University


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    objects = UserManager()
    is_active = models.BooleanField(default=True, verbose_name='Активность')
    is_confirmed = models.BooleanField(default=False, verbose_name='Подтвердил email')
    is_staff = models.BooleanField(default=False, verbose_name='Сотрудник')
    university = models.ForeignKey(University,
                                   on_delete=models.DO_NOTHING,
                                   verbose_name='Университет',
                                   related_name='users',
                                   blank=True,
                                   null=True)
    phone = models.CharField(max_length=20,
                             verbose_name='Номер телефона')
    transcript = models.FileField(verbose_name='Транскрипт',
                                  upload_to=transcript_path,
                                  blank=True,
                                  null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def send_confirmation_email(self,
                                subject='Подтверждение аккаунта ocenika.com',
                                message='Перейдите по ссылке чтобы подтвердить ваш акканут',
                                **kwargs):
        print('in_sending_email')
        token = Token.objects.get(user_id=self.id)
        EmailThread(subject, self.email, token.key, self.id, message, kwargs).start()
