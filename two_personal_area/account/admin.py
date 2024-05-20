from django.contrib import admin
from account import models

admin.site.register(models.Client)
admin.site.register(models.Employee)
admin.site.register(models.Customer)
