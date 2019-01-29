from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .forms import CommentForm
from .models import Post, Comment


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return HttpResponse('<h1>Blog About</h1>')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostListMLBView(ListView):

    def get_queryset(self):
        return Post.objects.all().filter(blog_type='MLB')

    model = get_queryset
    context_object_name = 'posts'
    template_name = 'blog/mlb_page.html'
    ordering = ['-date_posted']


class PostListNBAView(ListView):

    def get_queryset(self):
        return Post.objects.all().filter(blog_type='NBA')

    model = get_queryset
    context_object_name = 'posts'
    template_name = 'blog/nba_page.html'
    ordering = ['-date_posted']


class PostListNFLView(ListView):

    def get_queryset(self):
        return Post.objects.all().filter(blog_type='NFL')

    model = get_queryset
    context_object_name = 'posts'
    template_name = 'blog/nfl_page.html'
    ordering = ['-date_posted']


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/home.html'
    ordering = ['-date_posted']


class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'
    slug_url_kwarg = 'blog_id'

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


def PostCommentView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

def PostCommentApproveView(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

def PostCommentRemoveView(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)
