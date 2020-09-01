from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import RegisterForm, PoolForm
from .models import Pool, Categories


def index(request):
    pool = Pool.objects.all().order_by('-date_add')

    return render(request, 'home/index.html', {
        'pool': pool,
        }
    )


def vote(request, img_id):
    if request.user.is_authenticated:

        try:
            img = Vote.objects.get(pk=img_id)
            pool = Pool.objects.get(title=img.name)
            if request.method == 'POST':
                img.vote += 1
                img.save()
                return HttpResponseRedirect(f'../../detail/{pool.id}/')
            else:
                return HttpResponseRedirect(reverse('home:not_found'))

        except (KeyError, Vote.DoesNotExist):
            return HttpResponseRedirect(reverse('home:not_found'))

        except (KeyError, Pool.DoesNotExist):
            return HttpResponseRedirect(reverse('home:not_found'))
            
    else:
        return HttpResponseRedirect(reverse('home:login_status'))


def add_thumbnails(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PoolForm(request.POST, request.FILES)
            print(form.is_valid())
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                return HttpResponseRedirect(reverse('home:index'))
        else:
            form = PoolForm()
        return render(request, 'home/add_thumnails.html', {
            'form' : form,
        }
        )
    else:
        return HttpResponseRedirect(reverse('home:login_status'))


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


def not_found(request):
    return render(request, 'home/404.html')