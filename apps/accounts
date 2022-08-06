
from django.urls import path,include

from rest_framework.authtoken.views import obtain_auth_token

from .views import CreateUserView,LoginUserView,UserResetPasswordView



app_name = 'api'

urlpatterns = [ 
    path('token/', obtain_auth_token, name='get_token'),
    path('signup/', CreateUserView.as_view(), name='signup'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('password_reset/', UserResetPasswordView.as_view(), name='password_reset'),
    ]
