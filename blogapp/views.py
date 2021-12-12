from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blogapp.models import Post
from django.urls import reverse_lazy
# Create your views here.
class HomeView(ListView):
    model = Post
    template_name='index.html'
    order=['-date']

class DetailView(DetailView):
    model=Post
    template_name='detail.html'

class AddPostView(CreateView):
    model=Post
    template_name='add_post.html'
    fields='__all__' 

class UpdatePostView(UpdateView):
    model=Post
    template_name='edit.html'
    fields=['title','body']

class DeletePostView(DeleteView):
    model=Post
    template_name='delete.html'
    success_url=reverse_lazy('blogapp:index')