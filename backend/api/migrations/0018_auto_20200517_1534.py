# Generated by Django 2.1.7 on 2020-05-17 09:34

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20200517_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professorreview',
            name='moderator_message',
            field=models.CharField(default='', max_length=500, verbose_name='Сообщение от системы'),
        ),
        migrations.AlterField(
            model_name='professorreview',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.Subject', verbose_name='Предмет'),
        ),
        migrations.AlterField(
            model_name='professorreview',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='professor_reviews', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='professorreview',
            name='value',
            field=models.PositiveSmallIntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Оценка'),
        ),
    ]