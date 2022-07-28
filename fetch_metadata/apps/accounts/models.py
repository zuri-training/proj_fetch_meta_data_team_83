from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify

from .managers import CustomUserManager


# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length = 50, unique = True)
    email = models.EmailField(('Email address'),unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = CustomUserManager() #add the manager that will create a user and create a super user
    class Meta:
        ordering = ["username","date_joined"]
        verbose_name = "User"

    def __str__(self):
        return self.username

    # Creating a default slug/username for users if blank.
    def get_absolute_url(self):
        """
        Create a default url for each user using their username
        """

        return reverse('user_detail', kwargs={'slug': slugify(self.username)})


def get_upload_path(instance, filename):
    return '{0}/profile'.format(instance.user.id)


class CustomUserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True, blank=True, upload_to=get_upload_path)
    job_type=models.CharField(max_length=100, null=True, blank=True)
    bio=models.TextField(null=True,blank=True)
