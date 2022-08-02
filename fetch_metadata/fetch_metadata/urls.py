from django.urls import path,include


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
<<<<<<< HEAD
    path('api/', include('api.urls')),
    path('', include('apps.commons.urls')),
   
 
=======
    path('', include('api.urls')),
>>>>>>> 19c0b860c49171c68bbe00245034a835e1c1d5e9
]