from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth import get_user_model

UserModel = get_user_model()
class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = UserCreationForm.Meta.fields + ('email',)


class CustomUserLoginForm(AuthenticationForm):
    class Meta:
        model = UserModel
        fields = ['username','password']


class UploadForm():
    pass

class ProfileForm():
    pass

class ChangePasswordForm():
    pass

