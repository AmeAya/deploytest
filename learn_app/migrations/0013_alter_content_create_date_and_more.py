# Generated by Django 4.1.2 on 2022-10-27 22:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn_app', '0012_alter_content_create_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 27, 22, 15, 4, 45824, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='purchasehistory',
            name='purchase_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 27, 22, 15, 4, 42795, tzinfo=datetime.timezone.utc)),
        ),
    ]