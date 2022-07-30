from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

def home_page(request):
    """
    A view to fetch the homepage
    """
    return render(request, "common/home.html")

def about(request):
    """
    A view to fetch the about page
    """
    return render(request, "common/about.html")


class HomeView(ListView):
    model = Post
    template_name = 'common/index.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'common/article_details.html'