from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm,PasswordChangeForm
from django.forms import ModelForm
from django.contrib.auth import get_user_model, authenticate
from .models import CustomUserProfile

UserModel = get_user_model()

#CustomUserProfile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = '__all__'


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields =[ 'username','email',]

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

class CustomUserProfileCreationForm(ModelForm):
    class Meta:
      model = CustomUserProfile
      fields = ['profile_pic','job_type','bio']

    def clean_avatar(self):

        profile_pic = self.cleaned_data['profile_pic']

        try:
            w, h = get_image_dimensions(profile_pic)

            #validate dimensions
            max_width = max_height = 1000
            if w > max_width or h > max_height:
                raise forms.ValidationError(
                    u'Please use an image that is '
                     '%s x %s pixels or smaller.' % (max_width, max_height))

            #validate content type
            main, sub = profile_pic.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, '
                    'GIF or PNG image.')

            #validate file size
            if len(profile_pic) > (20 * 1024):
                raise forms.ValidationError(
                    'Profile picture file size may not exceed 20kb.')

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new avatar
            """
            pass

        return profile_pic

class ShowUserForm(ModelForm):
    class Meta:
        model = UserModel
        fields= ["username","email"]
