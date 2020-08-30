from django.db import models
from django.contrib.auth.models import User

class Categories(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Pool(models.Model):
    date_add = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=30)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    img_sample = models.ImageField(upload_to='static/sample/')
    def __str__(self):
        return self.title
    
    def deactive(self):
        self.status=False
        self.save()


class Vote(models.Model):
    name = models.ForeignKey(Pool, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/upload_tumb/')
    vote = models.IntegerField(default=0)
    