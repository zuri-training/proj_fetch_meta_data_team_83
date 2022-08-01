from django.urls import path,include
from .views import CreateUserView,LoginUserView

from rest_framework.authtoken.views import obtain_auth_token
from . import views

app_name = 'api'

urlpatterns = [
    path('token/', obtain_auth_token, name='get_token'),
    path('signup/', CreateUserView.as_view(), name='signup'),
    path('login/', LoginUserView.as_view(), name='login'),
]
