from django import forms

from django.contrib.auth.forms import UserCreationForm

from newspaper.models import Redactor, Newspaper


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


class NewspaperForm(forms.ModelForm):
    class Meta:
        model = Newspaper
        fields = '__all__'

    publishers = forms.ModelMultipleChoiceField(
        queryset=Redactor.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Publishers:',
    )
