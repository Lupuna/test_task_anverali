import shutil
import tempfile
from django.test import TestCase
from django.conf import settings
from account.models import Client, Employee, Customer


class SettingsCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user_client = Client.objects.create_user(
            username='test_username_1',
            password='test_password_1',
        )

        cls.employee = cls.user_client.employee
        cls.customer = cls.user_client.customer
