# Generated by Django 2.1.7 on 2020-05-16 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_professorreview_moderator_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivacyPolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='', verbose_name='Документ')),
            ],
            options={
                'verbose_name': 'Политика конфиденциальности',
            },
        ),
    ]
