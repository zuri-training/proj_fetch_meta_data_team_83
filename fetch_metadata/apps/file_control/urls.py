
from django import urls
from django.urls import path,include
from . import views

app_name='file'
urlpatterns = [
    path('',views.FileListView.as_view(), name='userFileList'),
    path('dashboard/',views.FileCreateView.as_view(), name='userFileUpload'),
    path('<int:pk>/', views.FileDetailView.as_view(), name='file_detail'),
    # path('test/', views.read_file, name='fileDetail'),
]
