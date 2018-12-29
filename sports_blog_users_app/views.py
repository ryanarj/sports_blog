from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.
def register(request):
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login(request):
    form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})
