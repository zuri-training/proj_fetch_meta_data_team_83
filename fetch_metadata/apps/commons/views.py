from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView

def home_page(request):

    return render(request, "common/index.html")

def about(request):

    return render(request, "common/about.html")



class HomeView(ListView):
    model = Post
    template_name = 'common/index.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'common/article_details.html'

class AddPostView(CreateView):
    model = Post
    template_name = 'common/post.html'
    field = '__all_-'