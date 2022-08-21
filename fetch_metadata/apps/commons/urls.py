from django.urls import path
from django.views.generic.base import RedirectView


from .views import HomeView, HowItWorksView, CreateDocumentationView, UpdateDocumentationView, DeleteDocumentationView, ServicePage,AboutUs,DocumentationView

app_name = 'common'
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("dashboard/", RedirectView.as_view(url="/file/dashboard"), name="dashboard"),
    path("services/", ServicePage.as_view(), name = 'services'),
    path("about-us/", AboutUs.as_view(), name = 'about_us'),
    path('create_docs/',CreateDocumentationView.as_view(), name='create_docs'),
    path("how_it_works/", HowItWorksView.as_view(), name = 'how_it_works'),
    path("<slug:slug>/", DocumentationView.as_view, name="documentation"),
    path('article/edit/<int:pk>/', UpdateDocumentationView.as_view(), name = 'update'),
    path('article/<int:pk>/remove/', DeleteDocumentationView.as_view(), name = 'delete'),
]
