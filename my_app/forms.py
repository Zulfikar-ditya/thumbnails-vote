from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Pool


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
        ]



class PoolForm(forms.ModelForm):
    img_1 = forms.ImageField(label='Image 1')
    img_2 = forms.ImageField(label='Image 2')
    class Meta:
        model = Pool
        fields = (
            'title',
            'categories',
            'img_1',
            'img_2',
        )
