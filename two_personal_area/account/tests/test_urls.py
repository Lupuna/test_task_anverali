from django.test import SimpleTestCase
from django.urls import resolve, reverse
from account import views as account_views


class TestUrls(SimpleTestCase):

    def test_employee_profile_url_is_resolve(self):
        url = reverse('account:employee_profile')
        self.assertEqual(resolve(url).func.view_class, account_views.EmployeeProfile)

    def test_customer_profile_url_is_resolve(self):
        url = reverse('account:customer_profile')
        self.assertEqual(resolve(url).func.view_class, account_views.CustomerProfile)

    def test_update_client_profile_url_is_resolve(self):
        url = reverse('account:update_client_profile')
        self.assertEqual(resolve(url).func.view_class, account_views.UpdateClientProfile)

    def test_client_profile_url_is_resolve(self):
        url = reverse('account:client_profile')
        self.assertEqual(resolve(url).func.view_class, account_views.ClientProfile)
