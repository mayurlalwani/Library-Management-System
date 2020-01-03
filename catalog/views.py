from django.shortcuts import render
from catalog.models import Book, BookInstance, Author, Genre
from django.views import generic
# Create your views here.


class BookListView(generic.ListView):
    model = Book

    def get_queryset(self):
        return Book.objects.filter(title__icontains='war')[:5]  # Get 5 books containing the title war


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.count()

    context = {
        'num-books' : num_books,
        'num_instances': num_instances,
        'num_instances_available':num_instances_available,
        'num_authors' : num_authors,

    }

    return render(request, 'index.html', context=context)