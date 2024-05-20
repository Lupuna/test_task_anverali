import shutil
import tempfile
from django.test import TestCase
from django.conf import settings
from account.models import Client, Employee, Customer


class SettingsCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client.objects.create_user(
            username='test_username_1',
            password='test_password_1',
        )

        cls.employee = cls.client.employee
        cls.customer = cls.client.customer
