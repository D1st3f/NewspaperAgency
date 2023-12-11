from django.contrib import admin
from django.urls import path, include

from newspaper.views import register, PostsSearchView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", register, name="register"),
    path("search/", PostsSearchView.as_view(), name="posts-search"),
    path("", include("newspaper.urls", namespace="newspaper")),
]
