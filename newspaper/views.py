from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from newspaper.forms import RegistrationForm, NewspaperForm
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


class PostsSearchView(generic.ListView):
    model = Newspaper
    template_name = "newspaper/newspaper_list.html"
    paginate_by = 6

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Newspaper.objects.filter(title__icontains=query) | Newspaper.objects.filter(content__icontains=query)
        else:
            return Newspaper.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        return context


@method_decorator(staff_member_required, name='dispatch')
class PostsUpdateView(generic.UpdateView):
    model = Newspaper
    form_class = NewspaperForm

    def get_success_url(self):
        return reverse_lazy('newspaper:posts-detail', kwargs={'pk': self.object.pk})


class PostsDeleteView(generic.DetailView):
    model = Newspaper
    success_url = reverse_lazy("newspaper:posts-detail")


class TopicListView(generic.ListView):
    model = Topic
    paginate_by = 2


class TopicDetailView(generic.DetailView):
    model = Topic
