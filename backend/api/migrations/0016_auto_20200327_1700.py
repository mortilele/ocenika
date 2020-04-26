# Generated by Django 2.1.7 on 2020-03-27 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_subject_abbreviation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='abbreviation',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Аббревиатура'),
        ),
        migrations.AlterField(
            model_name='university',
            name='name',
            field=models.CharField(max_length=500, verbose_name='Название'),
        ),
    ]
