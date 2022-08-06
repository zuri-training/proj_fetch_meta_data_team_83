from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token

from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('api-auth/', include('rest_framework.urls')),
    path('', include('api.urls')),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
    path('', include('apps.commons.urls')),
    path('file/', include('apps.file_control.urls')),
    path('accounts/', include('apps.accounts.urls')),
    path('token/', obtain_auth_token, name='get_token'),
    path('bucket/',include('buckets.urls')),
    path('test/', include('buckets.test.urls'))
]
>>>>>>> 03cfc020ac4957cf993bd3b245054da035351c5b
