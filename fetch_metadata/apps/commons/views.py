from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.

#def home_page(request):
   #return render(request, "common/home.html", {})

def about(request):
    return render(request, "common/about.html")

class HomeView(ListView):
    model = Post
    template_name = 'common/home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'common/article_details.html'
    