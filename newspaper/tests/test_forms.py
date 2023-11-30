from django.test import TestCase
from newspaper.forms import RegistrationForm, NewspaperForm, ContactForm
from newspaper.models import Redactor, Topic


class RegistrationFormTest(TestCase):
    def test_registration_form_valid_data(self):
        form_data = {
            "username": "john_doe",
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "password1": "securepassword",
            "password2": "securepassword",
        }
        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_registration_form_invalid_data(self):
        form_data = {
            "username": "",
            "first_name": "John",
            "last_name": "Doe",
            "email": "invalid_email",
            "password1": "password",
            "password2": "different_password",
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("username", form.errors)
        self.assertIn("email", form.errors)
        self.assertIn("password2", form.errors)


class NewspaperFormTest(TestCase):
    def test_newspaper_form_valid_data(self):
        redactor = Redactor.objects.create(username="john_doe")
        topic = Topic.objects.create(name="Science")

        form_data = {
            "title": "Breaking News",
            "content": "Important information.",
            "image": None,
            "topic": [topic.id],
            "publishers": [redactor.id],
        }
        form = NewspaperForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_newspaper_form_invalid_data(self):
        form_data = {
            "title": "",
            "content": "",
            "image": None,
            "topic": [],
            "publishers": [],
        }
        form = NewspaperForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors)
        self.assertIn("content", form.errors)
        self.assertIn("topic", form.errors)
        self.assertIn("publishers", form.errors)


class ContactFormTest(TestCase):
    def test_contact_form_valid_data(self):
        form_data = {
            "email": "john.doe@example.com",
            "message": "Hello, this is a test message.",
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_contact_form_invalid_data(self):
        form_data = {
            "email": "invalid_email",
            "message": "",
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)
        self.assertIn("message", form.errors)
