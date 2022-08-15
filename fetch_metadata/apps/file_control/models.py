import os,io
from django.db import models
from django.core.files import File as Filer
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from .tasks import create_metadata
from .filechecker import ContentTypeRestrictedFileField
from .storage import OverwriteStorage
from .readfile import read_file
from .exifcreator import create_meta_file

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
class File(models.Model):

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE) #the user object that owns  file

    file = ContentTypeRestrictedFileField(upload_to=user_directory_path,content_types=content_types, max_upload_size=max_upload_size)
    created_at = models.DateTimeField(auto_now_add=True)
    meta_file = models.FileField(upload_to = user_directory_path, null=True,blank=True)

    # def filename(self):
    #     return os.path.basename(self.file.name)

    # def filesize(self):
    #     pass
    # def file_extension(self):
    #     pass
    # def filetype(self):
    #     pass
    # def filedetails(self):
    #     pass

    def get_absolute_url(self):
        """
        The url for each file
        Can be accessed through file_details
        """
        return reverse('file:file_detail', kwargs={'pk': self.id})

    @property
    def get_file_full_path(self):
        return self.file.url
    
    
        



# @receiver(pre_save, sender=File)
# def file_update(sender, **kwargs):
#     """
#     If a file contains double names, remove the old name before saving a new one
#     """
#     file_instance = kwargs['instance']
#     if file_instance.file:
#         path = file_instance.file.path
#         os.remove(path)

@receiver(pre_save, sender=File)
def save_meta_file(sender,**kwargs):
    """
    Create the metadata file and populate the database
    """
    print(f"sender: {sender}")
    print(f"kwargs: {kwargs}")
    file_main = kwargs["instance"]
    file_instance = user_directory_path(file_main, str(file_main.file))
    # file_instance = str(kwargs["instance"].file)
    # file_instance = kwargs["instance"].file.path
    print(f"file_instance.file.path: {file_instance}")
    print(f"file_main: {file_main}")
    # create_meta_file(file_instance)
    file_ext = ".mttrck" #metatrack file extension for saving metadata
    root_file_name = os.path.splitext(file_instance)[0] #file name without extension


    output_file = root_file_name+file_ext #join the rootname and extension
    media_path = settings.MEDIA_ROOT #get the media root
    final_output = os.path.relpath(output_file,media_path) #get the relative path

    # File.objects.filter(id=file_main.id).update(meta_file=str(final_output))
    file_main.meta_file=(output_file)
    print(f"outputfile: {output_file}")
    print(f"outputfilewithjoin: {os.path.join(media_path,output_file)}")
    # create_meta_file(str(os.path.join(media_path,output_file)))

@receiver(post_save, sender=File)
def make_meta(sender, **kwargs):
    create_metadata.delay(kwargs['instance'].file.path)
