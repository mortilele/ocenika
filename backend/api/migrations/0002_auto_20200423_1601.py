# Generated by Django 2.1.7 on 2020-04-23 16:01

from django.db import migrations, models
import django.db.models.deletion
import utils.file_upload


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfessorRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('review', models.TextField(default='', verbose_name='Отзыв')),
                ('value', models.PositiveSmallIntegerField(blank=True, default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Оценка преподавателя',
                'verbose_name_plural': 'Оценки преподавателя',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Название предмета')),
                ('abbreviation', models.CharField(blank=True, max_length=300, null=True, verbose_name='Аббревиатура')),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предметы',
            },
        ),
        migrations.AddField(
            model_name='professor',
            name='avatar',
            field=models.ImageField(default='noavatar.png', null=True, upload_to=utils.file_upload.professor_path, verbose_name='Аватар'),
        ),
        migrations.AddField(
            model_name='professor',
            name='average_rating',
            field=models.PositiveIntegerField(default=0, verbose_name='Средний рейтинг'),
        ),
        migrations.AddField(
            model_name='professor',
            name='rating_count',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество оценок'),
        ),
        migrations.AddField(
            model_name='university',
            name='abbreviation',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Аббревиатура'),
        ),
        migrations.AddField(
            model_name='university',
            name='logo',
            field=models.ImageField(default='noimage.png', null=True, upload_to=utils.file_upload.university_path, verbose_name='Лого'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='patronymic',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='universities',
            field=models.ManyToManyField(to='api.University', verbose_name='Университеты в котором он преподает'),
        ),
        migrations.AlterField(
            model_name='university',
            name='name',
            field=models.CharField(max_length=500, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='subject',
            name='professors',
            field=models.ManyToManyField(related_name='subjects', to='api.Professor', verbose_name='Преподаватели этого предмета'),
        ),
        migrations.AddField(
            model_name='subject',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='api.University'),
        ),
        migrations.AddField(
            model_name='professorrating',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='api.Professor', verbose_name='Преподаватель'),
        ),
    ]