# Generated by Django 4.1.2 on 2022-10-25 10:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_alter_post_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 25, 10, 48, 50, 893150)),
        ),
    ]