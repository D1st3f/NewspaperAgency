from django import forms
from django.contrib.auth.forms import UserCreationForm

from newspaper.models import Redactor


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Redactor
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2']
