from django.shortcuts import render
from django.views.generic import ListView
from .models import Book

# Create your views here.
class BookList(ListView):
    model = Book
    template_name = 'books/index.html'
    context_object_name = "books"