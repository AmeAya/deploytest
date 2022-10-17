# Generated by Django 4.1.2 on 2022-10-17 10:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_course_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/images')),
                ('text', models.TextField()),
                ('datetime', models.DateTimeField(default=datetime.datetime(2022, 10, 17, 10, 48, 19, 747803))),
            ],
        ),
    ]