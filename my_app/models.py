from django.db import models
from django.contrib.auth.models import User


class Categories(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Pool(models.Model):
    date_add = models.DateField(auto_now=True, auto_now_add=False)
    title = models.CharField(max_length=30)

    categories = models.ForeignKey(Categories ,on_delete=models.CASCADE)

    status = models.BooleanField(default=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def deactive(self):
        self.status=False
        self.save()


class Vote(models.Model):
    name = models.ForeignKey(Pool, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/upload_tumb/')
    vote = models.IntegerField(default=0)


class Image(models.Model):
    name = models.ForeignKey(Pool, on_delete=models.CASCADE)
    models.ImageField(upload_to='static/upload_tumb/', height_field=1300, width_field=700, max_length=None)
