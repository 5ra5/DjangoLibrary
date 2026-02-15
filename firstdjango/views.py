from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import BookForm, AuthorForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

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

def view_all_authors(request):
    all_authors = Author.objects.all()
    return render(request, 'all_authors.html', {'authors' : all_authors})

@login_required
def add_book(request):    
    if request.method == 'POST':  
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_books')
    else:
        form = BookForm()

    return render(request, 'add_book.html', {'form': form})

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_authors')
    else:
        form = AuthorForm()

    return render(request, 'add_author.html', {'form' : form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form' : form})