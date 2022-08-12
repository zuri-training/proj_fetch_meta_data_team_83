from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth import get_user_model,views
from .forms import SignupForm,CustomUserLoginForm#, PasswordResetForm,ChangePasswordForm,
from .permissions import IsCreatorOrAdminReadOnly
from django.urls import reverse_lazy


# Create your views here.

UserModel = get_user_model()

class CreateUserView(CreateView):
    success_url = reverse_lazy('api:login')
    form_class = SignupForm
    template_name = 'api/signup.html'

class LoginUserView(views.LoginView):
    template_name = 'api/login.html'
    form_class = CustomUserLoginForm
    next_page = 'api:userFileUpload'


class LogoutUserView(views.LogoutView):
    template_name = 'common/home.html'
    next_page = '/home/'

class UserPasswordChangeView(views.PasswordChangeView):
    template_name = 'api/password_change.html'
    # form_class = ChangePasswordForm
    success_url="password_change_done"

class UserResetPasswordView(views.PasswordResetView):
    template_name='api/password_reset.html'
    # form_class = PasswordResetForm