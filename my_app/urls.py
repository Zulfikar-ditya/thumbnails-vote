from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_thumbnails, name='add'),
    path('register/', views.register, name='register'),
    path('login_status/', views.login_status, name='login_status'),
    path('404/', views.not_found, name='not_found'),
    path('my_thumbnails/', views.my_thumbnails, name='my_thumbnails'),
    path('edit/<int:pool_id>/', views.edit_thumb, name='edit,')
]   