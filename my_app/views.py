from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import RegisterForm
from .models import Pool, Vote


def index(request):
    pool = Pool.objects.all().order_by('-id')
    img = Vote.objects.get(name=pool[0].title)
    # fill = img.filter(name=pool[0].title)
    print(img)
    
    return render(request, 'home/index.html', {
        'pool': pool,
        'img': img,
        }
    )


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
        return HttpResponseRedirect('../login/')

