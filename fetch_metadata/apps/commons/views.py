from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.base import RedirectView

from django.urls import reverse_lazy
from .forms import PostForm, EditForm
from .models import Post

class HomeView(ListView):
    """
    Include a summary of how it works in a list
    """
    model = Post
    template_name = 'common/home.html'

class DashboardView(RedirectView):
    # pattern_name="file:userFileUpload"
    pass

class HowItWorksView(ListView):
    model = Post
    template_name = 'common/how_it_works.html'
    

class CreateDocumentationView(PermissionRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'common/add_post.html'


class UpdateDocumentationView(PermissionRequiredMixin, UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'common/update_post.html'
    #fields = ['title', 'title_tag', 'body']


class DeleteDocumentationView(PermissionRequiredMixin, DeleteView):
    model = Post
    template_name = 'common/delete_post.html'
    success_url = reverse_lazy('home')


class ServicePage(ListView):
    model = Post
    template_name = 'common/service.html'

class AboutUs(ListView):
    model = Post
    template_name = 'common/about_us.html'

class DocumentationView(DetailView):
    model = Post
    template_name = 'common/documentation.html'
