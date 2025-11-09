from django.shortcuts import render
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .models import Book,Author
from django.views.generic import CreateView, View, ListView

def books_list(request):
    books = Book.objects.all()
    paginator = Paginator(books , 10)
    page_number = request.GET.get('page' , 1)
    page_ogj = paginator.get_page(page_number)
    return render(request,"books/books_list.html",{'books':books})

def book_details(request,pk):
    book = Book.objects.get(pk=pk)
    return render(request,"books/book_details.html",{'book':book})

def author_details(request,pk):
    author = Author.objects.get(pk=pk)
    return render(request,"books/author_details.html",{'author':author})


class CreateAuthor(CreateView):
    model = Author
    fields = "__all__"
    template_name = "books/create_author.html"
    success_url = reverse_lazy('books_list')



