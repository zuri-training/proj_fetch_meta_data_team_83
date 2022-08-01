
from django import forms
from .models import file_Upload

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = file_Upload
        fields = ['file',]