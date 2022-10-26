from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime

# Create your models here.
class Student(models.Model):
    last_name = models.CharField(max_length=50, null=False, blank=False)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=True, blank=True, unique=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)

    def __str__(self):
        return str(self.last_name) + ' ' + str(self.first_name)

class Course(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    image = models.ImageField(null=True, blank=True)
    price_per_month = models.IntegerField(null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    duration = models.IntegerField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(null=True, blank=True)
    text = models.TextField(null=False, blank=False)
    datetime = models.DateTimeField(default=datetime.now(), null=False, blank=False)

    def __str__(self):
        return self.title
