from django.conf.urls.static import static
from django.urls import path

from newspaper.views import (index,
                             contact_us,
                             PostsListView,
                             PostsCreateView,
                             PostsDetailView,
                             PostsUpdateView,
                             PostsDeleteView,
                             TopicListView,
                             TopicDetailView,
                             TopicCreateView,
                             TopicUpdateView,
                             TopicDeleteView, delete_topic_from_newspaper, )
from newspaper_agency import settings

urlpatterns = [
    path("", index, name="index"),
    path('contact-us/', contact_us, name='contact_us'),
    path("posts/", PostsListView.as_view(), name='posts-list'),
    path("posts/create/", PostsCreateView.as_view(), name='posts-create'),
    path("posts/<int:pk>/update/",
         PostsUpdateView.as_view(),
         name='posts-update'),
    path("posts/<int:pk>/delete/",
         PostsDeleteView.as_view(),
         name='posts-delete'),
    path("posts/<int:pk>/", PostsDetailView.as_view(), name='posts-detail'),
    path("topic/", TopicListView.as_view(), name='topic-list'),
    path("topic/<int:pk>/", TopicDetailView.as_view(), name='topic-detail'),
    path("topic/create/", TopicCreateView.as_view(), name='topic-create'),
    path("topic/<int:pk>/update/",
         TopicUpdateView.as_view(),
         name='topic-update'),
    path("topic/<int:pk>/delete/",
         TopicDeleteView.as_view(),
         name='topic-delete'),
    path("posts/<int:post_id>/delete-topic/<int:topic_id>/",
         delete_topic_from_newspaper,
         name='delete-topic-from-newspaper'),
]

app_name = "newspaper"
