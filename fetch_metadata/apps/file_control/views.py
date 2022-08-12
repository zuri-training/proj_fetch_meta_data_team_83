import os
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,ListView, DetailView
from .forms import FileUploadForm
from .models import File
from .tasks import create_metadata
from django.urls import reverse_lazy
from django.shortcuts import render


# Create your views here.
#upload files
class FileCreateView(LoginRequiredMixin, CreateView):
    """
    Generates the view where the user can upload their files
    LoginRequiredMixin: Requires that the user has appropriate permissions
    """
    form_class = FileUploadForm
    success_url = reverse_lazy('/file_detail/')
    template_name = 'file_control/dashboard.html'


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user

        # get the instance of the file that will be used to create the metadata
        # model_instance = File.objects.first().file
        # print(model_instance)

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

def read_file(request, file_path):
    """
    Read the metadata from the file and retuens to the user.
    args:
    file_path = path to saved metadata file

<<<<<<< HEAD
    """
=======
class FileDetailView(LoginRequiredMixin, DetailView):
    model = File
    template_name = 'file_detail_view.html'


def read_file(request):
>>>>>>> dev

    with open(file_path, 'r') as f:
        file_content = f.readlines()
        result = [item.split(':', 1) for item in file_content]
        f.close()
        context = {'meta_data': result}
        return (context)




class FileDetailView(LoginRequiredMixin, DetailView):
    model = File
    template_name = 'file_detail_view.html'

    def get_context_data(self):
        context = super(File, self).get_context_data(**kwargs)
        context["meta_data"]= read_file(self.request, Task.objects.filter(meta_file=self.object.file))
        return context


# class MetadataView(LoginRequiredMixin, ListView):
#     template_name = 'file_control/extraction_page.html'
#     # context_object_name = 'meta_data'

#     def get_queryset(self):
#         self.meta_data = get_object_or_404(File, user=self.kwargs['user'])
#         return File.objects.filter(meta_data__file=self.kwargs['file'])


#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         # Add in the publisher
#         context['meta_data'] = self.meta_data
#         return context
