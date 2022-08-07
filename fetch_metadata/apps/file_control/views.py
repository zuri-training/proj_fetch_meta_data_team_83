from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,ListView, DetailView
from .forms import FileUploadForm
from .models import FileUpload
from django.urls import reverse_lazy


# Create your views here.
#upload files
class FileCreateView(LoginRequiredMixin, CreateView):
    """
    Generates the view where the user can upload their files
    PermissionRequiredMixin: Requires that the user has appropriate permissions
    """
    form_class = FileUploadForm
    success_url = reverse_lazy('userFileList')
    template_name = 'dashboard.html'

    # def get_form_kwargs(self):
        # kwargs = super(FileCreateView, self).get_form_kwargs()
        # kwargs['user'] = self.request.user
    #     return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        return super(FileCreateView, self).form_valid(form)

#files list
class FileListView(LoginRequiredMixin, ListView):
    model = FileUpload
    template_name = 'file.html'
    context_object_name = 'file'
    permission_required='list_file_upload'

class FileDetailView(LoginRequiredMixin, DetailView):
    model = FileUpload
    permission_required='view_file_upload'
    template_name = 'file_detail_view.html'
