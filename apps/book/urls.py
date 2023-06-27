from django.urls import path
from .views import create_author, list_authors


urlpatterns = [
    path('create_author/', create_author, name='create_author'),
    path('list_authors/', list_authors, name="list_authors")
]
