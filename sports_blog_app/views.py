from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Post

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return HttpResponse('<h1>Blog About</h1>')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostListView(ListView):
    def get_queryset(self):
        # original qs
        qs = super().get_queryset() 
        # filter by a variable captured from url, for example
        return qs.filter(name__startswith=self.kwargs['blog_type'])
    def get_slug_field(self):
        """
        Get the name of a slug field to be used to look up by slug.
        """
        return self.slug_field

    query_blog_name = get_queryset
    model = Post
    if query_blog_name == 'MLB':
        template_name = 'blog/mlb_page.html'
    else:
        template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete_confirm.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
