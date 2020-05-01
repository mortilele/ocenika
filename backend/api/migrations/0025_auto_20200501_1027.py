# Generated by Django 2.1.7 on 2020-05-01 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_auto_20200430_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='professors',
            field=models.ManyToManyField(blank=True, null=True, related_name='subjects', to='api.Professor', verbose_name='Преподаватели этого предмета'),
        ),
    ]
