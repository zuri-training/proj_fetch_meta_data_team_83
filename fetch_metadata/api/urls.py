from django.contrib import admin
from django.urls import path,include

from rest_framework.authtoken.views import obtain_auth_token

from .views import CreateUserView,LoginUserView



app_name = 'api'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', obtain_auth_token, name='get_token'),
    path('signup/', CreateUserView.as_view(), name='signup'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('', include('apps.commons.urls')),
    path('file/', include('apps.file_control.urls')),
]
