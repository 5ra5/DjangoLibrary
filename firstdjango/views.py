from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def view_all_books(request):
    all_books = Book.objects.all()
    return render(request, 'all_books.html', {'books' : all_books})

def view_single_book(request, bookid):
    single_book = get_object_or_404(Book, id=bookid)
    return render(request, 'single_book.html', {'book' : single_book})

def view_books_by_year(request, bookyear):
    filtered_books = Book.objects.all().filter(year=bookyear)
    return render(request, 'all_books.html', {'books' : filtered_books})

def view_books_by_category(request, bookcategory):
    category_books = Book.objects.filter(category=bookcategory)
    return render(request, 'books_by_category.html', {'category' : category_books})

def view_books_by_year_and_category(request, bookyear, bookcategory):
    category_year = Book.objects.all().filter(category=bookcategory, year=bookyear)
    return render(request, 'all_books.html', {'books' : category_year})
