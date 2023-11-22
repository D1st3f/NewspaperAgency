from django.urls import path

from newspaper.views import index, ConctactsList

urlpatterns = [
    path("", index, name="index"),
    path("contacts/", ConctactsList.as_view(), name='contacts')
]

app_name = "newspaper"
