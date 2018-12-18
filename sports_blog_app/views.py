from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return HttpResponse('<h1>Blog About</h1>')

posts = [
    {
    'author' : 'Ryan',
    'title' : 'Sell the Knicks',
    'content' : 'THe knicks need to be sold!!',
    'date_posted' : '12/18/2018'
    }
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)
