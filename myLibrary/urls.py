from django.urls import path
from myLibrary.views import show_library, borrow_books, get_borrowed_books_user, get_favorite_books_user
from myLibrary.views import show_library, borrow_books, get_borrowed_boks, return_book, return_damaged_book

app_name = 'myLibrary'

urlpatterns = [
    path("library/", show_library, name="show_library"),
    path("borrow-books/<int:book_id>", borrow_books, name="borrow_books"),
    path("get_borrowed_books_user/", get_borrowed_books_user, name="get_borrowed_books_user"),
    path("get_favorite_books_user/<int:user_id>", get_favorite_books_user, name="get_favorite_books_user"),
    path("get-borrowed-books/", get_borrowed_boks, name="get_borrowed_books"),
    path("return-book/<int:book_id>", return_book, name="return_book"),
    path("return-damaged-book/<int:book_id>", return_damaged_book, name="return_book"),
    
]