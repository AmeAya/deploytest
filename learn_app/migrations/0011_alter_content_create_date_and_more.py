# Generated by Django 4.1.2 on 2022-10-27 22:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn_app', '0010_remove_subscription_cost_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 27, 22, 14, 54, 1780, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='purchasehistory',
            name='purchase_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 27, 22, 14, 53, 999074, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='duration_days',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='price',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
