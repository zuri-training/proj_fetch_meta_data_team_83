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

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            self.user_cache = authenticate(email=email,
  password=password)
            if self.user_cache is None:
                self.user_cache = authenticate(email=email, password=password)
                raise forms.ValidationError(
                        self.error_messages['invalid_login'],
                        code='invalid_login',
                        params={'username': self.username_field.verbose_name},
                   )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data


class UploadForm():
    pass

class ProfileForm():
    pass

class ChangePasswordForm(PasswordChangeForm):
    pass


class PasswordResetForm():
    pass
