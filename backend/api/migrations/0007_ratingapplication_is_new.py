# Generated by Django 2.1.7 on 2020-05-08 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_ratingapplication_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratingapplication',
            name='is_new',
            field=models.BooleanField(default=True, verbose_name='Рассмотрен?'),
        ),
    ]