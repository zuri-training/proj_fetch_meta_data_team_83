from django.contrib import admin
from .models import Post
#from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model

User= get_user_model()

class PostAdmin (admin.ModelAdmin):
    list_display = ["title"]
    search_fields =["title", "body"]
    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)
