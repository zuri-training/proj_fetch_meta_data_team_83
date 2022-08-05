
from django.urls import path,include
from .views import CreateUserView,LoginUserView,UserResetPasswordView



app_name = 'api'

urlpatterns = [

    path('signup/', CreateUserView.as_view(), name='signup'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('', include('apps.commons.urls')),
    path('password_reset/', UserResetPasswordView.as_view(), name='password_reset'),
    ]
