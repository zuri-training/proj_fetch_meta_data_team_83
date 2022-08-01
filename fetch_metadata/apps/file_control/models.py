
from django.db import models

# Create your models here.
class file_Upload(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='file_control/documents/')
    created_at = models.DateTimeField(auto_now_add=True)