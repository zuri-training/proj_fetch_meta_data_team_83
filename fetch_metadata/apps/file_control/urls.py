<<<<<<< HEAD
=======

>>>>>>> 03cfc020ac4957cf993bd3b245054da035351c5b
from django import urls
from django.urls import path
from . import views

app_name='file'
urlpatterns = [
    path('',views.FileListView.as_view(), name='userFileList'),
    path('dashboard/',views.FileCreateView.as_view(), name='userFileUpload'),
    path('download/<int:pk>', views.FileDetailView.as_view(), name='download'),
<<<<<<< HEAD
    path('bucket/',include('buckets.urls')),
=======
    path('bucket/',include('buckets.urls')),
]
>>>>>>> 03cfc020ac4957cf993bd3b245054da035351c5b
