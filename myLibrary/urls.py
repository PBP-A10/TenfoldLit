from django.urls import path
from myLibrary.views import borrow_books_flutter, show_library, borrow_books, get_borrowed_books, get_favorite_books
from myLibrary.views import show_library, borrow_books, get_borrowed_boks, return_book, return_damaged_book

app_name = 'myLibrary'

urlpatterns = [
    path("library/", show_library, name="show_library"),
    path("borrow-books/<int:book_id>", borrow_books, name="borrow_books"),
    path("borrow-books-flutter/<int:book_id>", borrow_books_flutter, name="borrow_books"),
    path("get-borrowed-books/", get_borrowed_boks, name="get_borrowed_books"),
    path("return-book/<int:book_id>", return_book, name="return_book"),
    path("return-damaged-book/<int:book_id>", return_damaged_book, name="return_book"),
    path("get_borrowed_books/<int:user_id>", get_borrowed_books, name="get_borrowed_books"),
    path("get_favorite_books/<int:user_id>", get_favorite_books, name="get_favorite_books"),
]