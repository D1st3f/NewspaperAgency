from django.conf.urls.static import static
from django.urls import path

from newspaper.views import (index,
                             ConctactUsListView,
                             PostsListView,
                             PostsCreateView,
                             PostsDetailView,
                             PostsUpdateView,
                             PostsDeleteView,
                             TopicListView,
                             TopicDetailView, )
from newspaper_agency import settings

urlpatterns = [
    path("", index, name="index"),
    path("contacts/", ConctactUsListView.as_view(), name='contacts'),
    path("posts/", PostsListView.as_view(), name='posts-list'),
    path("posts/create/", PostsCreateView.as_view(), name='posts-create'),
    path("posts/<int:pk>/update/", PostsUpdateView.as_view(), name='posts-update'),
    path("posts/<int:pk>/delete/", PostsDeleteView.as_view(), name='posts-delete'),
    path("posts/<int:pk>/", PostsDetailView.as_view(), name='posts-detail'),
    path("topic/", TopicListView.as_view(), name='topic-list'),
    path("topic/<int:pk>/", TopicDetailView.as_view(), name='topic-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

app_name = "newspaper"
