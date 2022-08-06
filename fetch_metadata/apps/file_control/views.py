from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView,ListView, DetailView
from .forms import FileUploadForm
from .models import file_Upload
from django.urls import reverse_lazy
import os
from django.conf import settings
from django.http import HttpResponse, Http404


# Create your views here.
#upload files
class FileCreateView(PermissionRequiredMixin,CreateView):
    """
    Generates the view where the user can upload their files
    PermissionRequiredMixin: Requires that the user has appropriate permissions
    """
    model = file_Upload
    form_class = FileUploadForm
    success_url = reverse_lazy('userFileList')
    template_name = 'dashboard.html'

#files list
class FileListView(PermissionRequiredMixin, ListView):
    model = file_Upload
    template_name = 'home.html'
    context_object_name = 'files'

class FileDetailView(PermissionRequiredMixin, DetailView):
    model = file_Upload
    template_name = 'file_detail_view.html'

