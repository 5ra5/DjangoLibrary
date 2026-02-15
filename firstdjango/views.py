from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import BookForm, AuthorForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test

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
@user_passes_test(lambda u: u.is_staff)
def add_book(request):    
    if request.method == 'POST':  
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.added_by = request.user
            book.save()
            return redirect('all_books')
    else:
        form = BookForm()

    return render(request, 'add_book.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_staff)
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.added_by = request.user
            author.save()
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

@login_required
def edit_book(request, bookid):
    # Get the book or return 404 if it doesn't exist
    book = get_object_or_404(Book, id=bookid)

    # Check authorization: must be staff OR the person who added it
    if not request.user.is_staff and book.added_by != request.user:
        return HttpResponseForbidden("You can only edit books you added.")
    
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book) # Pre-fill with existing book
        if form.is_valid():
            form.save()
            return redirect('single_book', bookid=book.id)
    else:
        form = BookForm(instance=book) # Pre-fill with existing book

    return render(request, 'edit_book.html', {'form' : form, 'book' : book})


@login_required
def delete_book(request, bookid):
    book = get_object_or_404(Book, id=bookid)

    if not request.user.is_staff and book.added_by != request.user:
        return HttpResponseForbidden("You can only delete books you added.")
    
    if request.method == 'POST':
        book.delete()
        return redirect('all_books')
    
    return render(request, 'confirm_delete.html', {'book' : book})