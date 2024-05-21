from django.core.exceptions import ValidationError
from account.tests.test_base import SettingsCase


class TestModels(SettingsCase):

    def test_str_method_client(self):
        self.assertEqual(str(self.user_client), str(self.user_client))

    def test_phone_regex_validator(self):
        with self.assertRaises(ValidationError):
            self.user_client.phone = '89dddd000'
            if self.user_client.full_clean():
                self.user_client.save()

    def test_str_method_employee(self):
        self.assertEqual(self.employee.client.username, str(self.employee))

    def test_str_method_customer(self):
        self.assertEqual(self.customer.client.username, str(self.customer))

