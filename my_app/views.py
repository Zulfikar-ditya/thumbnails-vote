from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import RegisterForm
from .models import Pool, Vote


def index(request):
    pool = Pool.objects.all().order_by('-date_add')

    return render(request, 'home/index.html', {
        'pool': pool,
        }
    )


def detail(request, id_pool):
    if request.user.is_authenticated:
        
        try:
            pool = Pool.objects.get(id=id_pool)
            img = Vote.objects.filter(name=pool.id)

            img1 = img[0]
            img2 = img[1]

            if pool.status == False:
                message = 'this thumbnail does not exist'
            else:
                message = None
            
            return render(request, 'home/detail.html', {
                'pool': pool,
                'img1': img1,
                'img2': img2,
                'message': message,
                }
            )

        except (KeyError, Pool.DoesNotExist):
            message = 'this thumbnail does not exist'
            return render(request, 'home/detail.html', {
            'message' : message
            }
        )

    else:
        return HttpResponseRedirect(reverse('home:login_status'))


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
    if request.method == "POST":
        print()
    else:
        pass
    return render(request, 'home/add_thumnails.html')


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