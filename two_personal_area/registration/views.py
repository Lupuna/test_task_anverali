from django.views.generic import CreateView
from registration.forms import SignUpForm
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('registration:login')
    template_name = 'registration/sing_up.html'
