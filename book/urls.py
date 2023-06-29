from django.urls import path
from .views import CreateAuthorView, ListAuthorsView, UpdateAuthorView, DeleteAuthorView

app_name = 'book'

urlpatterns = [
    path('create_author/', CreateAuthorView.as_view(), name='create_author'),
    path('list_authors/', ListAuthorsView.as_view(), name="list_authors"),
    path('edit_author/<int:pk>', UpdateAuthorView.as_view(), name="edit_author"),
    path('delete_author/<int:pk>', DeleteAuthorView.as_view(), name="delete_author")
]
