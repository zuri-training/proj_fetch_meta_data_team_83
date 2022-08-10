
from django import forms
from .models import File

class FileUploadForm(forms.ModelForm):
    class Meta:
      model = File
      fields = ['file',]

    # def __init__(self, *args, **kwargs):
        # user = kwargs.pop('user')
        # super(FileUploadForm, self).__init__(*args, **kwargs)
        # self.fields['user'].queryset = FileUpload.objects.filter(user=user)
