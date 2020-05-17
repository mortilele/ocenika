# Generated by Django 2.1.7 on 2020-05-17 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20200517_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='university',
            field=models.ManyToManyField(blank=True, related_name='subjects', to='api.University', verbose_name='Университеты'),
        ),
        migrations.AlterField(
            model_name='university',
            name='rating',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Рейтинг'),
        ),
    ]
