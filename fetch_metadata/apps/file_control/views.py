from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import ListView
from .models import file_Upload
from django.urls import reverse_lazy


# Create your views here.
#upload files
class fileCreateView(CreateView):
    model = file_Upload
    fields = ('author', 'title', 'file',)
    success_url = reverse_lazy('userFileList')
    template_name = 'file.html'
    
#files list
class fileListView(ListView):
    model = file_Upload
    template_name = 'home.html'
    context_object_name = 'files'

#download files
# class downloadFilesView(CreateView):


#from django.contrin.auth import get_user_model
#user = get_user_model