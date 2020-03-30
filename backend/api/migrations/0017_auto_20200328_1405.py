# Generated by Django 2.1.7 on 2020-03-28 14:05

from django.db import migrations, models
import utils.file_upload


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20200327_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='avatar',
            field=models.ImageField(default='noavatar.png', null=True, upload_to=utils.file_upload.professor_path, verbose_name='Аватар'),
        ),
    ]