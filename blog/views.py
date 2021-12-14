from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post


class BlogListView(ListView):
    model = Post
    context_object_name = "PostList"
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    context_object_name = "PostDetail"
    template_name = 'post_detail.html'
