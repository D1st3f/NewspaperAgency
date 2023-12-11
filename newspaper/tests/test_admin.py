from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from newspaper.models import Redactor, Newspaper, Topic


class AdminPanelTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.admin_user = get_user_model().objects.create_user(
            username="admin",
            password="adminpassword",
            is_staff=True,
            is_superuser=True
        )

        self.redactor = Redactor.objects.create(
            username="john_doe",
            first_name="John",
            last_name="Doe"
        )
        self.topic = Topic.objects.create(name="Science")
        self.newspaper = Newspaper.objects.create(
            title="Breaking News",
            content="Important information."
        )

    def test_admin_login(self):
        login_url = reverse("admin:login")
        response = self.client.get(login_url)
        self.assertEqual(response.status_code, 200)

        login_data = {
            "username": "admin",
            "password": "adminpassword",
        }
        response = self.client.post(login_url, data=login_data, follow=True)
        self.assertTrue(response.context["user"].is_authenticated)
        self.assertEqual(response.status_code, 200)

    def test_admin_edit_object(self):
        self.client.login(username="admin", password="adminpassword")

        redactor_edit_url = reverse(
            "admin:newspaper_redactor_change",
            args=[self.redactor.id]
        )
        response = self.client.get(redactor_edit_url)
        self.assertEqual(response.status_code, 200)
