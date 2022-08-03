from django.urls import path


from .views import HomeView, HowItWorksView, CreateDocumentationView, UpdateDocumentationView, DeleteDocumentationView

app_name = 'commons'
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("docs/<slug:slug>", HowItWorksView.as_view(), name = 'how_it_works'),
    path('create_docs/',CreateDocumentationView.as_view(), name='create_docs'),
    path('article/edit/<int:pk>', UpdateDocumentationView.as_view(), name = 'update'),
    path('article/<int:pk>/remove', DeleteDocumentationView.as_view(), name = 'delete'),
]
