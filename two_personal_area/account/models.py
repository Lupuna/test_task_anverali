from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.utils.translation import gettext_lazy as _
from django.db import models


class Client(AbstractUser):
    phone = models.PositiveIntegerField(_('phone number'), blank=True, null=True)

    def __str__(self):
        return self.username


class Employee(models.Model):
    client = models.OneToOneField(Client, on_delete=models.PROTECT, related_name='employee')
    employee_rating = models.PositiveIntegerField(default=100, validators=[
        MaxValueValidator(100),
    ])

    def __str__(self):
        return self.client.username


class Customer(models.Model):
    client = models.OneToOneField(Client, on_delete=models.PROTECT, related_name='customer')
    customer_rating = models.PositiveIntegerField(default=100, validators=[
        MaxValueValidator(100),
    ])

    def __str__(self):
        return self.client.username
