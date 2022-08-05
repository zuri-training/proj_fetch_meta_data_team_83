
from django import urls
from django.urls import path
from . import views

app_name='file'
urlpatterns = [
    path('',views.FileListView.as_view(), name='userFileList'),
    path('dashboard/',views.FileCreateView.as_view(), name='userFileUpload'),
    path('download/<int:pk>', views.FileDetailView.as_view(), name='download'),
    path('bucket/',include('buckets.urls')),
]
