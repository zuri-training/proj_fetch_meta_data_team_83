from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView,ListView, DetailView
from .forms import FileUploadForm
from .models import FileUpload
from django.urls import reverse_lazy


# Create your views here.
#upload files
class FileCreateView(PermissionRequiredMixin, CreateView):
    """
    Generates the view where the user can upload their files
    PermissionRequiredMixin: Requires that the user has appropriate permissions
    """
    form_class = FileUploadForm
    success_url = reverse_lazy('userFileList')
    template_name = 'dashboard.html'
    permission_required='add_file_upload'

#files list
class FileListView(PermissionRequiredMixin, ListView):
    model = FileUpload
    template_name = 'file.html'
    context_object_name = 'file'
    permission_required='list_file_upload'

class FileDetailView(PermissionRequiredMixin, DetailView):
    model = FileUpload
    permission_required='view_file_upload'
    template_name = 'file_detail_view.html'

