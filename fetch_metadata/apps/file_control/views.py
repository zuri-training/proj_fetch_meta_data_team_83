from django.shortcuts import render
from django.views.generic import CreateView,ListView
from .forms import FileUploadForm
from .models import FileUpload
from django.urls import reverse_lazy


# Create your views here.
#upload files
class FileCreateView(CreateView):
    model = FileUpload
    form_class = FileUploadForm
    success_url = reverse_lazy('userFileList')
    template_name = 'file.html'
    
#files list
class FileListView(ListView):
    model = FileUpload
    template_name = 'home.html'
    context_object_name = 'files'

#download files
# class downloadFilesView(CreateView):
