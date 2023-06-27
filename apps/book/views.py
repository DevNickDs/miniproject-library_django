from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
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
    authors = Author.objects.filter(state = True)
    return render(request, 'book/list_authors.html', {'authors': authors})

def edit_author(request, id, author_form=None, error=None):
    try:
        author = Author.objects.get(id = id)
        if request.method == 'GET':
            author_form = AuthorForm(instance = author)
        else:
            author_form = AuthorForm(request.POST, instance = author)
            if author_form.is_valid:
                author_form.save()
            return redirect('Home')
    except ObjectDoesNotExist as e:
        error = e
    
    return render(request, 'book/create_author.html', {'author_form': author_form, 'error': error})

def delete_author(request, id):
    author = Author.objects.get(id = id)
    if request.method == 'POST':
        author.state = False
        author.save()
        return redirect('book:list_authors')
    return render(request, 'book/delete_author.html', {'author': author})