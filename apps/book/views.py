from django.shortcuts import render, redirect
from .forms import AuthorForm
from .models import Author

# Create your views here.

def home(request):
    return render(request, 'index.html')

def create_author(request):
    if request.method == 'POST':
        #print(request.POST)
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect('Home')
    else:
        author_form = AuthorForm()
        #print(author_form)
    return render(request, 'book/create_author.html', {'author_form': author_form})

def list_authors(request):
    authors = Author.objects.all()
    return render(request, 'book/list_authors', {'authors': authors})