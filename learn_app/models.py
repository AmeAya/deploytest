from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.timezone import now

# Create your models here.
class Subscription(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, null=False)
    purchase_time = models.DateTimeField(default=now(), blank=False, null=False)
    expire_date = models.DateTimeField(blank=False, null=False)
    cost = models.PositiveIntegerField(
        validators=[MinValueValidator(0)]
    )

    def __str__(self):
        return 'id:' + str(self.user_id) + ' exp_date:' + str(self.expire_date)

class LearnUser(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, null=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=True, blank=True, unique=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)

    def __str__(self):
        return str(self.last_name) + ' ' + str(self.first_name)

class Category(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    image = models.ImageField(null=True, blank=True)
    preview = models.TextField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class Content(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField()
    create_date = models.DateTimeField(default=now(), null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)
    video = models.FileField(upload_to='videos/', null=False, blank=False)

    def __str__(self):
        return self.title
