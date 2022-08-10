
from django import forms
<<<<<<< HEAD
from .models import file_Upload

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = file_Upload
        fields = ['file',]
=======
from .models import File

class FileUploadForm(forms.ModelForm):
    class Meta:
      model = File
      fields = ['file',]

    # def __init__(self, *args, **kwargs):
        # user = kwargs.pop('user')
        # super(FileUploadForm, self).__init__(*args, **kwargs)
        # self.fields['user'].queryset = FileUpload.objects.filter(user=user)
>>>>>>> origin/main
