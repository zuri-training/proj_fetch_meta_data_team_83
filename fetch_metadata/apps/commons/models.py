from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.template.defaultfilters import slugify

UserModel = get_user_model()
class Post(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.CharField(max_length = 255)
    title_tag = models.CharField(max_length = 255, null=True)
    body = models.TextField()
    slug = models.SlugField(max_length=255)
    created_on = models.DateField(auto_now_add=True)
    
    # class Meta:
    #     default_permissions = ()
    #     permissions = (
    #         ("add_post", "Can add post"),
    #         ("change_post", "Can change a posts"),
    #         ("delete_post", "Can delete a posts"),
    #         ("view_post", "Can view a particular posts"),
    #         ("list_posts", "Can list all posts"),
    #     )

    def __str__(self):
        return self.title

   # Creating a default slug/username for users if blank.
    def get_absolute_url(self):
        """
        Create a default url for each post using their slug
        """
        return reverse('documentation_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        # Check for a slug
        if not self.slug:
            # Create default slug
            self.slug = slugify(self.title)
        # Finally save.
        super().save(*args, **kwargs)

class Faq(models.Model):
    faqQuest = models.CharField(max_length=255)
    faqAnswer = models.TextField()
    slug = models.SlugField(max_length=255, default='faqs')
    def __str__(self):
        return self.faqQuest
    def get_absolute_url(self):
        """
        Create a default url for each faq
        """
        return reverse('faq_detail', kwargs={'slug':self.slug})
    def save(self, *args, **kwargs):
        # Check for a slug
        if not self.slug:
            # Create default slug
            self.slug = slugify(self.faqQuest)
        # Finally save.
        super().save(*args, **kwargs)
