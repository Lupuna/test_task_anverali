from django.contrib.auth.forms import UserCreationForm
from account.models import Client


class SignUpForm(UserCreationForm):
    class Meta:
        model = Client
        fields = ('username', 'password1', 'password2')
