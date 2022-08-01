from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import ModelForm
from .models import CustomUser #CustomUserProfile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = '__all__'


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = '__all__'

# class CustomUserProfileForm(ModelForm):
#     class Meta:
#         model = CustomUserProfile
#         fields = '__all__'
