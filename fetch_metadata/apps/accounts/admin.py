from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.models import Group

UserModel = get_user_model()
class CustomUserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    fieldsets = (
        (None, {
            'fields': ('username','email', )}),
            ('Personal info', {
                'fields': ('first_name', 'last_name')}),
                ('Permissions', {
                    'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
                    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff'),
            }),
            )
    list_display = ['email', 'username', 'is_staff', 'is_superuser',]
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('username', )
admin.site.register(UserModel, CustomUserAdmin)
admin.site.unregister(Group)
