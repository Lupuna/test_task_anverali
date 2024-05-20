from django.db.models.signals import post_save
from django.dispatch import receiver
from account.models import Client, Employee, Customer


@receiver(post_save, sender=Client)
def client_post_save(sender, instance, created, **kwargs):
    if created:
        Employee.objects.create(client=instance)
        Customer.objects.create(client=instance)
