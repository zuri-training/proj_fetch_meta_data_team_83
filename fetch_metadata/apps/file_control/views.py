import os
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,ListView, DetailView
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
from .forms import FileUploadForm
from .models import File
from .tasks import create_metadata
from .readfile import read_file
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required



# Create your views here.

#Home view
# @login_required
# def dashboardview(request):
#     context ={}

#     # add the dictionary during initialization
#     form = FileUploadForm(request.POST or None)
#     if form.is_valid():
#         form.save()

#     context['form'] = form
#     context["file_list"] = File.objects.filter(user=request.user)

#     return render(request, "common/dashboard.html", context)
# upload files
class FileCreateView(LoginRequiredMixin, CreateView):
    """
    Generates the view where the user can upload their files
    LoginRequiredMixin: Requires that the user has appropriate permissions
    """
    form_class = FileUploadForm
    # success_url = reverse_lazy('/file_detail/') #redirect the user to file details page
    template_name = 'file_control/dashboard.html'

    def get_success_url(self):
        print(self.object.id)
        return reverse_lazy('file:file-detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        # context["file_list"] = user.file.all()
        # filelist =
        context["file_list"] = File.objects.filter(user=self.request.user)
        return context


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

# class getmetadata(LoginRequiredMixin, DetailView):
#     model=File
#     # request should be ajax and method should be POST.
#     def get_context_data(self):
#         context = super().get_context_data(**kwargs)

#         if self.request.is_ajax:
#             # read the file_content

#             fullfile = get_object_or_404(File, pk=pk) # get everything in that row in the database
#             metafile = fullfile.meta_file #return jusst the meta_file
#             path = os.path.join(settings.MEDIA_ROOT, metafile.path) #get the full path

#             metadata = read_file(request, path)
#             context["meta_data"]= metadata


class FileDetailView(LoginRequiredMixin, DetailView):
    model = File
    template_name = 'file_control/extraction_page.html'

    def get_context_data(self, **kwargs):
        filepk = self.kwargs.get('pk') #get the primary key of the file
        fullfile = get_object_or_404(File, pk=filepk) # get everything in that row in the database

        #check if user is the owner of the file. Return none if not
        # if self.request.user is not fullfile.user:
        #     return None

        context = super().get_context_data(**kwargs)

        metafile = fullfile.meta_file #return jusst the meta_file
        path = os.path.join(settings.MEDIA_ROOT, metafile.path) #get the full path

        metadata = read_file(path)
        print(metadata)
        context["meta_data"]= metadata
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
