from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,ListView
from .forms import FileUploadForm
from .models import file_Upload
from django.urls import reverse_lazy
import os
from django.conf import settings
from django.http import HttpResponse, Http404


# Create your views here.
#upload files
class FileCreateView(LoginRequiredMixin,CreateView):
    model = file_Upload
    form_class = FileUploadForm
    success_url = reverse_lazy('userFileList')
    template_name = 'file.html'

#files list
class FileListView(LoginRequiredMixin, ListView):
    model = file_Upload
    template_name = 'home.html'
    context_object_name = 'files'

#download files

def download(request, path):
    print(path)
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.jpg")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
