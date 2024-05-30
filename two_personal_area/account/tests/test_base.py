from django.test import TestCase
from account.models import Client


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
