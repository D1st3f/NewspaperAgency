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


class ContactForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(label='Email Address')
    message = forms.CharField(label='Your Message', widget=forms.Textarea)
    agree_terms = forms.BooleanField(label='I agree to the Terms and Conditions', required=True)
