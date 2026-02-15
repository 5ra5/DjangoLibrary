# django app folder urls
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name='contact'),
    path('books/', views.view_all_books, name='all_books'),
    path('authors/', views.view_all_authors, name='all_authors'),
    path('books/add/', views.add_book, name='add_book'),
    path('authors/add/', views.add_author, name='add_author'),
    path('books/<int:bookid>', views.view_single_book, name='single_book'),
    path('books/year/<int:bookyear>', views.view_books_by_year, name='books_by_year'),
    path('books/category/<bookcategory>', views.view_books_by_category, name='books_by_category'),
    path('books/category/<bookcategory>/year/<int:bookyear>', views.view_books_by_year_and_category, name='books_by_year_and_category'),
    path('register/', views.register, name='register'),
]