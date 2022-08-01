
from django import forms
from .models import file_Upload

class file_Upload_Form(forms.ModelForm):
    class Meta:
        model = file_Upload
        fields = ['author', 'title', 'file',]