from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls')),
    path('', include('apps.commons.urls')),
    path('commons/', include('django.contrib.auth.urls')),


]


