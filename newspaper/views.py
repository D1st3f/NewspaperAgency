from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login
from django.db.models import Count, Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views import generic

from newspaper.forms import (RegistrationForm,
                             NewspaperForm,
                             ContactForm,
                             TopicForm, TopicUpdateForm)
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


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = ContactForm()

    return render(request, 'newspaper/contact_us.html', {'form': form})


def delete_topic_from_newspaper(request, post_id, topic_id):
    if request.method == 'POST':
        post = get_object_or_404(Newspaper, pk=post_id)
        topic = get_object_or_404(Topic, pk=topic_id)
        post.topic.remove(topic)
        return HttpResponseRedirect(reverse('newspaper:topic-detail',
                                            args=[topic_id]))


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
            return Newspaper.objects.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(topic__name__icontains=query)
            ).distinct()
        else:
            return Newspaper.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        return context


@method_decorator(staff_member_required, name='dispatch')
class PostsCreateView(generic.CreateView):
    model = Newspaper
    form_class = NewspaperForm

    def get_success_url(self):
        return reverse_lazy(
            'newspaper:posts-detail', kwargs={'pk': self.object.pk}
        )


@method_decorator(staff_member_required, name='dispatch')
class PostsUpdateView(generic.UpdateView):
    model = Newspaper
    form_class = NewspaperForm

    def get_success_url(self):
        return reverse_lazy(
            'newspaper:posts-detail', kwargs={'pk': self.object.pk}
        )


@method_decorator(staff_member_required, name='dispatch')
class PostsDeleteView(generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("newspaper:posts-list")


class TopicListView(generic.ListView):
    model = Topic
    paginate_by = 8
    template_name = 'newspaper/topic_list.html'

    def get_queryset(self):
        queryset = Topic.objects.annotate(
            newspaper_count=Count('newspaper')).filter(newspaper_count__gt=0)
        return queryset.order_by('name')


class TopicDetailView(generic.DetailView):
    model = Topic


@method_decorator(staff_member_required, name='dispatch')
class TopicCreateView(generic.CreateView):
    model = Topic
    form_class = TopicForm

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object = form.save()
        newspapers = form.cleaned_data.get('newspapers')
        if newspapers:
            self.object.newspaper.set(newspapers)
        return response

    def get_success_url(self):
        return reverse_lazy(
            'newspaper:topic-detail', kwargs={'pk': self.object.pk}
        )


@method_decorator(staff_member_required, name='dispatch')
class TopicUpdateView(generic.UpdateView):
    model = Topic
    form_class = TopicUpdateForm

    def get_success_url(self):
        return reverse_lazy(
            'newspaper:topic-detail', kwargs={'pk': self.object.pk}
        )


@method_decorator(staff_member_required, name='dispatch')
class TopicDeleteView(generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("newspaper:topic-list")
