from django import forms
from .models import Post
from django.contrib.auth import get_user_model


UserModel= get_user_model()
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        #model = get_user_model()
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            #'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
             'body': forms.Textarea(attrs={'class': 'form-control'}),
}

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        #model = get_user_model()
        fields = ('title', 'title_tag', 'body')

        widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control'}),
                'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
                'body': forms.Textarea(attrs={'class': 'form-control'}),
}