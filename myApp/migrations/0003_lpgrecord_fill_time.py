# Generated by Django 2.2.3 on 2019-08-02 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_lpgrecord_load_database_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='lpgrecord',
            name='fill_time',
            field=models.IntegerField(default=0, verbose_name='充装时间(分钟)'),
        ),
    ]
