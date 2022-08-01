
from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model

from .filechecker import ContentTypeRestrictedFileField

# Create your models here.
UserModel = get_user_model()
content_types = [
    'application/json',
    'application/pdf',
    'audio/mpeg',
    'image/png',
    'image/jpeg',
    'image/gif',
    'image/svg+xml',
    'text/csv',
    'audio/webm',
    ]
max_upload_size = 10485760 #10mb

def user_directory_path(instance, filename):
    """Creates a path for the user which is only accessible by the user

    Args:
        instance of type (CustomUser): The user that owns this file
        filename (name of file)): The name given to this file by our system
    """
    
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'user_{instance.user.id}/{filename}'
class FileUpload(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    file = ContentTypeRestrictedFileField(upload_to=user_directory_path, content_types=content_types, max_upload_size=max_upload_size)
    created_at = models.DateTimeField(auto_now_add=True)
