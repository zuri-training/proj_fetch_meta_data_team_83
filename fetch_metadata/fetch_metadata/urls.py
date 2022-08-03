from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('', include('apps.commons.urls')),
    path('<slug:user_slug>', include('apps.file_control.urls')),
]
