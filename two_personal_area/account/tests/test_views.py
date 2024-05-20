from django.urls import reverse
from django.test import Client, RequestFactory
from account.tests.test_base import SettingsCase
from account.views import EmployeeProfile, CustomerProfile, UpdateClientProfile, ClientProfile
from account.models import Client as ClientModel


class TestView(SettingsCase):

    def setUp(self):
        self.not_auth_client = Client()
        self.auth_client = Client()
        self.view_client = ClientModel.objects.get(id=1)
        self.auth_client.force_login(self.view_client)
        self.factory = RequestFactory()

    def test_customer_profile_view(self):
        url = reverse('account:employee_profile')
        template = 'account/employee_profile.html'
        request = self.factory.get(url)
        request.user = self.view_client
        with self.subTest('auth user, GET'):
            response = self.auth_client.get(url)
            self.assertEqual(200, response.status_code)
            self.assertTemplateUsed(response, template)

        with self.subTest('test get_object'):
            view = CustomerProfile()
            view.setup(request)
            correct_meaning = self.customer
            self.assertEqual(correct_meaning, view.get_object())

        with self.subTest('not auth user POST'):
            response = self.not_auth_client.get(url)
            self.assertEqual(302, response.status_code)

    def test_employee_profile_view(self):
        url = reverse('account:customer_profile')
        template = 'account/customer_profile.html'
        request = self.factory.get(url)
        request.user = self.view_client
        with self.subTest('auth user, GET'):
            response = self.auth_client.get(url)
            self.assertEqual(200, response.status_code)
            self.assertTemplateUsed(response, template)

        with self.subTest('test get_object'):
            view = EmployeeProfile()
            view.setup(request)
            correct_meaning = self.employee
            self.assertEqual(correct_meaning, view.get_object())

        with self.subTest('not auth user POST'):
            response = self.not_auth_client.get(url)
            self.assertEqual(302, response.status_code)

    def test_client_profile_view(self):
        url = reverse('account:client_profile')
        template = 'account/client_profile.html'
        request = self.factory.get(url)
        request.user = self.view_client
        with self.subTest('auth user, GET'):
            response = self.auth_client.get(url)
            self.assertEqual(200, response.status_code)
            self.assertTemplateUsed(response, template)

        with self.subTest('test get_object'):
            view = ClientProfile()
            view.setup(request)
            correct_meaning = self.view_client
            self.assertEqual(correct_meaning, view.get_object())

        with self.subTest('not auth user POST'):
            response = self.not_auth_client.get(url)
            self.assertEqual(302, response.status_code)

    def test_update_client_profile_view(self):
        url = reverse('account:client_profile')
        template = 'account/client_profile.html'
        request = self.factory.get(url)
        request.user = self.view_client
        with self.subTest('auth user, GET'):
            response = self.auth_client.get(url)
            self.assertEqual(200, response.status_code)
            self.assertTemplateUsed(response, template)

        with self.subTest('test get_object'):
            view = UpdateClientProfile()
            view.setup(request)
            correct_meaning = self.view_client
            self.assertEqual(correct_meaning, view.get_object())

        with self.subTest('not auth user POST'):
            response = self.not_auth_client.get(url)
            self.assertEqual(302, response.status_code)

