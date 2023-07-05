from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .models import Post


class PostListView(ListView):
    model = Post  # Берет данные из таблицы Post
    template_name = 'post_page.html'  # На какой template выгрежает данные
    context_object_name = 'Posts'  # По умолчанию, имя object


class PostDetailView(DetailView):  # DetailView требует чтобы ему передали pk
    model = Post
    template_name = 'post_detail_page.html'
    context_object_name = 'Post'


class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create_page.html'
    fields = ['title', 'author', 'body']


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete_page.html'
    success_url = reverse_lazy('posts_list')


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update_page.html'
    fields = ['title', 'body']
    # Убрал author, потому что не хочу давать его менять
