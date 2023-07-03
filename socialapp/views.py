from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


class PostListView(ListView):
    model = Post  # Берет данные из таблицы Post
    template_name = 'post_page.html'  # На какой template выгрежает данные
    context_object_name = 'Posts'  # По умолчанию, имя object
