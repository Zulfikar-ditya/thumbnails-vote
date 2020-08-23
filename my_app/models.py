from django.db import models
from django.contrib.auth.models import User


class Categories(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Pool(models.Model):
    date_add = models.DateField(auto_now=True, auto_now_add=False)
    title = models.CharField(max_length=30)

    img = models.ImageField(upload_to='static/upload_tumb/', height_field=None, width_field=None, max_length=None)
    img2 = models.ImageField(upload_to='static/upload_tumb/', height_field=None, width_field=None, max_length=None, blank=True)
    img3 = models.ImageField(upload_to='static/upload_tumb/', height_field=None, width_field=None, max_length=None, blank=True)

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
    vote_img_1 = models.IntegerField(null=True)
    vote_img_2 = models.IntegerField(null=True)
    vote_img_3 = models.IntegerField(null=True)
    def __str__(self):
        return self.name
