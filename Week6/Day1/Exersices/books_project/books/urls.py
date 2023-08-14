from django.urls import path
from .views import list_books, book_detail, create_book

urlpatterns = [
    path('books/', list_books, name='books'),
    path('book/<int:id>', book_detail, name="book"),
    path('create_book/', create_book, name='create_book')
]