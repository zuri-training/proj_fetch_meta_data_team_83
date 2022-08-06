from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm,PasswordChangeForm
from django.forms import ModelForm
from django.contrib.auth import get_user_model, authenticate

UserModel = get_user_model()

#CustomUserProfile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = '__all__'


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = '__all__'

# class CustomUserProfileForm(ModelForm):
#     class Meta:
#         model = CustomUserProfile
#         fields = '__all__'

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = UserCreationForm.Meta.fields + ('email',)


class CustomUserLoginForm(AuthenticationForm):
    class Meta:
        model = UserModel

class UploadForm(ModelForm):
    pass

class ProfileForm(ModelForm):
    pass

class ChangePasswordForm(PasswordChangeForm):
    pass


class PasswordResetForm():
    pass
