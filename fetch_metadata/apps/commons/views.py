from django.shortcuts import render

# Create your views here.

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