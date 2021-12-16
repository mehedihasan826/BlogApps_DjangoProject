from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Post


class BlogListView(ListView):
    model = Post
    context_object_name = "PostList"
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    context_object_name = "PostDetail"
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    context_object_name = "Create_Post"
    template_name = 'new_post.html'
    fields = ['title', 'author', 'body']


class BlogUpdateView(UpdateView):
    model = Post
    context_object_name = "edit_post"
    template_name = 'edit_post.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = Post
    context_object_name = "delete_post"
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

