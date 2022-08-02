from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django import forms
from django.contrib.auth import get_user_model, authenticate

UserModel = get_user_model()
class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = UserCreationForm.Meta.fields + ('email',)


class CustomUserLoginForm(AuthenticationForm):
    class Meta:
        model = UserModel
        fields = ['email','password']


class UploadForm():
    pass

class ProfileForm():
    pass

class ChangePasswordForm(PasswordChangeForm):
    pass


class PasswordResetForm():
    pass
