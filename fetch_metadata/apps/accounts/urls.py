
from django.urls import path,include
from django.contrib.auth import views as auth_views
from .views import UpdateUserView, ShowUser, CreateProfileView,CreateUserView,UserProfileDetails,LoginUserView,LogoutUserView,UserResetPasswordView, UserPasswordChangeView



app_name = 'api'

urlpatterns = [

    path('signup/', CreateUserView.as_view(), name='signup'),
    path('<slug:slug>/update', UpdateUserView.as_view(), name='update_user'),
    path('<slug:slug>/', ShowUser.as_view(), name='user_details'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('password_change/', UserPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name ='password_change_done'),
    path('password_reset/', UserResetPasswordView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_complete.html'), name ='password_reset_complete'),
    path('password_reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm'), name ='password_reset_confirm'),
    path('<slug:slug>/profile/edit', CreateProfileView.as_view(), name="edit_user_profile"),
    path('<slug:slug>/profile', UserProfileDetails.as_view(), name="edit_user_profile"),
    ]
