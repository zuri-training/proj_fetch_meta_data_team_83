from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# Create your views here.

UserModel= get_user_model()
def home_page(request):

    return render(request, "common/index.html")

def about(request):

    return render(request, "common/about.html")



class HomeView(ListView):
    model = Post
    template_name = 'common/index.html'
    odering = ['-id']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'common/article_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'common/add_post.html'
    #fields= '__all__'
    
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'common/update_post.html'
    #fields = ['title', 'title_tag', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'common/delete_post.html'
    success_url = reverse_lazy('home')


class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')