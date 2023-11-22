from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
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


class ConctactsList(generic.ListView):
    model = Topic
