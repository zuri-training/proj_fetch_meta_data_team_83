
from django import urls
from django.urls import path,include

from . import views

app_name='file'
urlpatterns = [
    path('',views.FileListView.as_view(), name='userFileList'),
    # path('dashboard/',views.dashboardview, name='userFileUpload'),
    path('dashboard/',views.FileCreateView.as_view(), name='userFileUpload'),
    path('<int:pk>/view', views.FileDetailView.as_view(), name='file-detail'),
    path('<int:pk>', views.detail_view, name='file-success'),
    # path('<int:pk>/meta', views.getmetadata.as_view(), name='meta-detail'),
]