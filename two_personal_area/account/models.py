from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator
from django.core.cache import cache
from django.db import models


class Client(AbstractUser):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(max_length=17, blank=True, null=True, validators=[
        phone_regex
    ])

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)


class Employee(models.Model):
    client = models.OneToOneField(Client, on_delete=models.PROTECT, related_name='employee')
    employee_rating = models.PositiveIntegerField(default=100, validators=[
        MaxValueValidator(100),
    ])

    def __str__(self):
        return self.client.username

    def save(self, *args, **kwargs):
        if cache.get(settings.EMPLOYEE_CACHE):
            cache.delete(settings.EMPLOYEE_CACHE)
        return super().save(*args, **kwargs)


class Customer(models.Model):
    client = models.OneToOneField(Client, on_delete=models.PROTECT, related_name='customer')
    customer_rating = models.PositiveIntegerField(default=100, validators=[
        MaxValueValidator(100),
    ])

    def __str__(self):
        return self.client.username

    def save(self, *args, **kwargs):
        if cache.get(settings.CUSTOMER_CACHE):
            cache.delete(settings.CUSTOMER_CACHE)
        return super().save(*args, **kwargs)
