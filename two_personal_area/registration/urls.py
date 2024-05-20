from django.urls import path
from django.contrib.auth import views as auth_views
from registration import views

app_name = 'registration'

urlpatterns = [
    path('sign-up/', views.SignUpView.as_view(), name='sign_up'),
    path('sign-in/', auth_views.LoginView.as_view(
        template_name='registration/login.html',
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
