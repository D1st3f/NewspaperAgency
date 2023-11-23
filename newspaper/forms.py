from django import forms

from django.contrib.auth.forms import UserCreationForm

from newspaper.models import Redactor, Newspaper, Topic


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


class TopicForm(forms.ModelForm):
    newspapers = forms.ModelMultipleChoiceField(
        queryset=Newspaper.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Topic
        fields = ['name', 'newspapers']


class ContactForm(forms.Form):
    email = forms.EmailField(label='Email Address')
    message = forms.CharField(label='Your Message', widget=forms.Textarea)
