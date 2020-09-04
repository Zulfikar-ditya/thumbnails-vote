from django.db import models
from django.contrib.auth.models import User

class Categories(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Pool(models.Model):
    date_add = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=30)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    img_1 = models.ImageField(upload_to='static/upload_tumb/')
    img_2 = models.ImageField(upload_to='static/upload_tumb/')

    vote_img1 = models.IntegerField(default=0)
    vote_img2 = models.IntegerField(default=0)
    def __str__(self):
        return self.title
    
    def deactive(self):
        self.status=False
        self.save()
    