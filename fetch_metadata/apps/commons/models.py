from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 
from django.contrib.auth import get_user_model


UserModel= get_user_model()
class Post(models.Model):
    title = models.CharField(max_length = 255)
    title_tag = models.CharField(max_length = 255)
    body = models.TextField()

    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    #updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    #timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')
 