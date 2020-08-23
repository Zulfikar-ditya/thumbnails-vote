from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import RegisterForm


def index(request):
    return render(request, 'home/index.html')


def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home:login_status'))
    else:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('../login/')
        else:
            form = RegisterForm()
        return render(request, 'registration/register.html', {'form': form,})


def login_status(request):
    if request.user.is_authenticated:
        return render(request, 'logged_in.html')
    
    else:
        return render(request, 'not_login.html')
