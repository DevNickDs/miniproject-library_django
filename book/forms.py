from django import forms
from .models import Author, Book

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'last_name', 'nationality', 'description']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'publish_date', 'author_id']