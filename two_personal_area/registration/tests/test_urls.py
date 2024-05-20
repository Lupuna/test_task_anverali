from django.test import SimpleTestCase
from django.urls import resolve, reverse
from django.contrib.auth import views as auth_views
from registration import views as registration_views


class TestUrls(SimpleTestCase):

    def test_sing_up_url_is_resolve(self):
        url = reverse('registration:sign_up')
        self.assertEqual(resolve(url).func.view_class, registration_views.SignUpView)

    def test_sing_in_url_is_resolve(self):
        url = reverse('registration:login')
        self.assertEqual(resolve(url).func.view_class, auth_views.LoginView)

    def test_log_out_url_is_resolve(self):
        url = reverse('registration:logout')
        self.assertEqual(resolve(url).func.view_class, auth_views.LogoutView)
