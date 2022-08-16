
from django import forms
from .models import File

class FileUploadForm(forms.ModelForm):
    file = forms.FileField(label="",widget=forms.FileInput(attrs={'class': "browse_button", "id":"input"}))
    def __init__(self, *args,**kwargs):
        self.file = forms.FileField(max_length=10,
                                        widget=forms.FileInput(attrs={'id': 'input',
                                                                      'class': 'browse_button'}))
        self.file.template_name_label = 'class="browse_button"' 
        super(FileUploadForm, self).__init__(*args, **kwargs)
    class Meta:
        model = File
        fields = ['file',]

    # def __init__(self, *args, **kwargs):
        # user = kwargs.pop('user')
        # super(FileUploadForm, self).__init__(*args, **kwargs)
        # self.fields['user'].queryset = FileUpload.objects.filter(user=user)
