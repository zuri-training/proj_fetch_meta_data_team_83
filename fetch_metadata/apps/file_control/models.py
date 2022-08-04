from apps.accounts.models import CustomUser
from django.db import models



# Create your models here.
class file_Upload(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='file_control/documents/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} is the title of this file attached to the user {self.author}'
    
