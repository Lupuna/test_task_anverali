from account import models
from account.tests.test_base import SettingsCase


class TestModels(SettingsCase):

    def test_str_method_client(self):
        self.assertEqual(str(self.client), str(self.client))

    def test_str_method_employee(self):
        self.assertEqual(self.employee.client.username, str(self.employee))

    def test_str_method_customer(self):
        self.assertEqual(self.customer.client.username, str(self.customer))

