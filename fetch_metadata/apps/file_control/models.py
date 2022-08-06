import os
import uuid
from django.db import models
from django.urls import reverse
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
    'image/jpg',
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

    def get_absolute_url(self):
        """
        The url for each file
        Can be accessed through file_details
        """
        return reverse('file_detail', kwargs={'pk': self.id})

    # class Meta:
    #     default_permissions = ()
    #     permissions = (
    #         ("add_file_upload", "Can upload file"),
    #         ("change_file_upload", "Can change the database of uploaded file"),
    #         ("delete_file_upload", "Can delete uploaded file"),
    #         ("view_file_upload", "Can view uploaded file"),
    #         ("list_file_upload", "Can list all uploaded file"),
    #     )

class MetaExtract(models.Model):
    file = models.OneToOneField(FileUpload, on_delete=models.CASCADE)
    meta_file = models.FileField(upload_to = user_directory_path)
