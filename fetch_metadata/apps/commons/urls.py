from django.urls import path 
from . import views 
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("article/<int:pk>", ArticleDetailView.as_view(), name = 'article-detail'),
    path('add_post/',AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name = 'update'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name = 'delete'),
]

    #path("about/", views.about, name='about')


