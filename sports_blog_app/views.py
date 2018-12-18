from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return HttpResponse('<h1>Blog About</h1>')

def home(request):
    return render(request, 'blog/home.html')
