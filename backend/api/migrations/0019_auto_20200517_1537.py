# Generated by Django 2.1.7 on 2020-05-17 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20200517_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professorreview',
            name='decline_reason',
            field=models.CharField(choices=[('Без причины', 'Еще не отказан'), ('Пожалуйста, обновите транскрипт', 'Обновите транскрипт'), ('Пожалуйста, прикрепите транскрипт', 'Прикрепите транскрипт'), ('Модерации не удалось удостоверить ваши данные', 'Не удалось удостоверить данные'), ('Пожалуйста, подтвердите почту', 'Почта не подтверждена'), ('Другая причина', 'Другая причина')], default='Без причины', max_length=500, verbose_name='Причина отказа'),
        ),
    ]