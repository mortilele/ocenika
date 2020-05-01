# Generated by Django 2.1.7 on 2020-04-30 13:37

from django.db import migrations, models
import utils.file_upload


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_auto_20200430_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='logo',
            field=models.ImageField(default='noimage.png', max_length=1000, null=True, upload_to=utils.file_upload.university_path, verbose_name='Лого'),
        ),
    ]