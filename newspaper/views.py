from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import generic

from newspaper.forms import RegistrationForm
from newspaper.models import Newspaper, Redactor, Topic


def index(request):
    num_post = Newspaper.objects.count()
    num_redactor = Redactor.objects.count()
    num_topic = Topic.objects.count()
    context = {
        "num_post": num_post,
        "num_redactor": num_redactor,
        "num_topic": num_topic,
    }
    return render(request, "newspaper/index.html", context=context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


class ConctactUsListView(generic.ListView):
    pass


class PostsListView(generic.ListView):
    model = Newspaper
    paginate_by = 6


class PostsDetailView(generic.DetailView):
    model = Newspaper


class TopicListView(generic.ListView):
    model = Topic
    paginate_by = 2


class TopicDetailView(generic.DetailView):
    model = Topic
