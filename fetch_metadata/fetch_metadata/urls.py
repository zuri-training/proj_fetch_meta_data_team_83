from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token

from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.commons.urls')),
    path('file/', include('apps.file_control.urls')),
    path('accounts/', include('apps.accounts.urls')),
    path('token/', obtain_auth_token, name='get_token'),
]