from django.contrib import admin

from .forms import EditForm, PostForm
from .models import Post


class PostAdmin (admin.ModelAdmin):
    list_display = ["title"]
    search_fields =["title", "body"]
    add_form = PostForm
    form = EditForm

    fieldsets = (
        (None, {
            'fields': ('title','title_tag', )}),
            ('Blog Post', {
                'fields': ('body',)}),
                ('Permissions', {
                    'fields': ('add_post', 'change_post', 'view_post', 'delete_posts', 'list_posts', 'groups', 'user_permissions')}),
                    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('title', 'title_tag', 'body',),
            }),
            )
    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)
