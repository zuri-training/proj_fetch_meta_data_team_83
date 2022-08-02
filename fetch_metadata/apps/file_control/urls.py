
from django.urls import path
from . import views



urlpatterns = [
    path('',views.FileListView.as_view(), name='userFileList'),
    path('create/',views.FileCreateView.as_view(), name='userFileUpload'),
]