# Generated by Django 2.1.7 on 2020-03-17 16:56

from django.db import migrations, models
import utils.models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200317_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professorrating',
            name='review',
            field=models.TextField(default='', verbose_name='Отзыв'),
        ),
        migrations.AlterField(
            model_name='professorrating',
            name='value',
            field=utils.models.IntegerRangeField(blank=True, default=0),
        ),
    ]
