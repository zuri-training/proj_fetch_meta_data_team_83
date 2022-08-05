from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('', include('apps.commons.urls')),
    path('files', include('apps.file_control.urls')),
    path('accounts', include('apps.accounts.urls')),
]
