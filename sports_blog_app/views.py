from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def about(request):
    return HttpResponse('<h1>Blog About</h1>')

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
