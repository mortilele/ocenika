# Generated by Django 2.1.7 on 2020-03-28 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20200328_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='patronymic',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='Отчество'),
        ),
    ]
