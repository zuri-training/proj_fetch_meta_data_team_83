from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,ListView, DetailView
from .forms import FileUploadForm
from .models import File
from . import exifcreator
from django.urls import reverse_lazy


# Create your views here.
#upload files
class FileCreateView(LoginRequiredMixin, CreateView):
    """
    Generates the view where the user can upload their files
    LoginRequiredMixin: Requires that the user has appropriate permissions
    """
    form_class = FileUploadForm
    success_url = reverse_lazy('/fileDetail/')
    template_name = 'file_control/dashboard.html'


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user

        # get the instance of the file that will be used to create the metadata
        model_instance = File.objects.first().file
        print(model_instance)


        return super(FileCreateView, self).form_valid(form)

    #create the exif file
    # exifcreator.create_meta_file(model_instance.path)


#files list
class FileListView(LoginRequiredMixin, ListView):
    # user = request.user
    model = File
    template_name = 'file_control/dashboard.html'
    context_object_name = 'file'
    def get_queryset(self):
        return File.objects.filter(file__user=self.kwargs['user'])


class FileDetailView(LoginRequiredMixin, DetailView):
    model = File
    template_name = 'file_detail_view.html'
