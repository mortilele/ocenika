# Generated by Django 2.1.7 on 2020-05-01 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_auto_20200501_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='professors',
            field=models.ManyToManyField(blank=True, related_name='subjects', to='api.Professor', verbose_name='Преподаватели этого предмета'),
        ),
    ]
