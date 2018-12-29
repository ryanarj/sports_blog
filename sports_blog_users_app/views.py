from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            username = form.cleaned_data.get('username')
            messages.success(request, f'User has been added')
    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form})

def login(request):
    form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})
