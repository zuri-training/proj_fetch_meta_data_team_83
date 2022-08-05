from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView,ListView, DetailView
from .forms import FileUploadForm
from .models import FileUpload
from django.urls import reverse_lazy


# Create your views here.
#upload files
class FileCreateView(PermissionRequiredMixin,CreateView):
    """
    Generates the view where the user can upload their files
    PermissionRequiredMixin: Requires that the user has appropriate permissions
    """
    model = FileUpload
    form_class = FileUploadForm
    success_url = reverse_lazy('userFileList')
    template_name = 'dashboard.html'

#files list
class FileListView(PermissionRequiredMixin, ListView):
    model = FileUpload
    template_name = 'home.html'
    context_object_name = 'files'
    def has_permission(self):
        user = self.request.user
        return user.has_perm('add_file_upload')

class FileDetailView(PermissionRequiredMixin, DetailView):
    model = FileUpload
    template_name = 'file_detail_view.html'
    def has_permission(self):
        user = self.request.user
        return user.has_perm(FileUpload.add_file_upload)
