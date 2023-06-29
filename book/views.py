from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from .forms import AuthorForm
from .models import Author
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView


# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

class CreateAuthorView(CreateView):
    model = Author
    template_name = "book/create_author.html"
    form_class = AuthorForm
    success_url = reverse_lazy('book:list_authors')

class ListAuthorsView(ListView):
    model = Author
    template_name = 'book/list_authors.html'
    context_object_name = 'authors'
    queryset = Author.objects.filter(state=True)

class UpdateAuthorView(UpdateView):
    model = Author
    template_name = "book/create_author.html"
    form_class = AuthorForm
    success_url = reverse_lazy('book:list_authors')

class DeleteAuthorView(DeleteView):
    model = Author
    template_name = "book/delete_author.html"
    def post(self, request, pk, *args, **kwargs):
        object = Author.objects.get(id=pk)
        object.state = False
        object.save()
        return redirect('book:list_authors')