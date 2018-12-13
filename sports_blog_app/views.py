from django.shortcuts import render
from django.http import HttpResponse
from .forms import ExampleForm

def about(request):
    return HttpResponse('<h1>Blog About</h1>')

def home(request):
    context = {'form': ExampleForm}
    return render(request, 'blog/home.html', context)
