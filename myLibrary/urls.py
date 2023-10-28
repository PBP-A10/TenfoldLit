from django.urls import path
from myLibrary.views import show_library, borrow_books, get_borrowed_boks, return_book

app_name = 'myLibrary'

urlpatterns = [
    path("library/", show_library, name="show_library"),
    path("borrow-books/<int:book_id>", borrow_books, name="borrow_books"),
    path("get-borrowed-books/", get_borrowed_boks, name="get_borrowed_books"),
    path("return-book/<int:book_id>", return_book, name="return_book"),
]