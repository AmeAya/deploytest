# Generated by Django 4.1.2 on 2022-10-27 22:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0022_alter_post_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 27, 22, 36, 56, 550011)),
        ),
    ]
