from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView, ListView
from django.contrib.auth import get_user_model,views
from .forms import SignupForm,CustomUserChangeForm,CustomUserLoginForm, CustomUserProfileCreationForm, ShowUserForm
from .permissions import IsCreatorOrAdminReadOnly
from .models import CustomUserProfile

# Create your views here.

UserModel = get_user_model()

class CreateUserView(CreateView):
    template_name = 'api/signup.html'
    form_class = SignupForm
    success_url = '/login/'


class UpdateUserView(LoginRequiredMixin, UpdateView):
    form_class = CustomUserChangeForm
    template_name = "api/update_user.html"
    success_url="/user_details/"

class ShowUser(LoginRequiredMixin, DetailView):
    form_class = ShowUserForm
    template_name = "api/user_details/"

class LoginUserView(views.LoginView):
    template_name = 'api/login.html'
    form_class = CustomUserLoginForm
    next_page = '/dashboard/'


class LogoutUserView(views.LogoutView):
    template_name = 'common/home.html'
    next_page = '/home/'

class UserPasswordChangeView(views.PasswordChangeView):
    template_name = 'api/password_change.html'
<<<<<<< HEAD
    form_class = ChangePasswordForm
    success_url="password_change_done"
=======

>>>>>>> 0859122e96e5754dbfeaaa2df1d1e6b498db3343

class UserResetPasswordView(views.PasswordResetView):
    template_name='api/password_reset.html'


class CreateProfileView(LoginRequiredMixin,CreateView):
    template_name = "api/edit_user_profile.html"
    form_class = CustomUserProfileCreationForm
    model = CustomUserProfile
    success_url = "/user_profile/"
    def form_valid(self):
      profile = form.save(commit=False)
      profile.user = self.request.user
      form.save()

class UserProfileDetails(LoginRequiredMixin, DetailView):
    template_name = "api/user_profile.html"
    model = CustomUserProfile

