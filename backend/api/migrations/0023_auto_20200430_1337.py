# Generated by Django 2.1.7 on 2020-04-30 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_auto_20200430_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='abbreviation',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Аббревиатура'),
        ),
    ]
