from django import urls
from django.urls import path, include
from . import views

app_name='file'
urlpatterns = [
    path('',views.FileListView.as_view(), name='userFileList'),
    path('dashboard/',views.FileCreateView.as_view(), name='userFileUpload'),
<<<<<<< HEAD
    path('download/<int:pk>', views.FileDetailView.as_view(), name='download'),

    path('bucket/',include('buckets.urls')),
=======
    path('<int:pk>/', views.FileDetailView.as_view(), name='fileDetail'),
    path('test/', views.read_file, name='fileDetail'),
>>>>>>> origin/main
]
