from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    #updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    #timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return self.title

 