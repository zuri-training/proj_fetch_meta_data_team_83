from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify

from .managers import CustomUserManager


# Create your models here.

class CustomUser(AbstractUser):
    # username = None #remove the default django username field
    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = ['email']
    objects = CustomUserManager() #add the manager that will create a user and create a super user
    class Meta:
        ordering = ["email","date_joined"]
        verbose_name = "User"

    def __str__(self):
        return self.username

    # Creating a default slug/username for users if blank.
    def get_absolute_url(self):
        """
        Create a default url for each user using their username
        """

        return reverse('user_detail', kwargs={'slug': self.username})

