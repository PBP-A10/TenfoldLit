from django.urls import path
from myLibrary.views import show_library, borrow_books, get_borrowed_books_user, get_favorite_books_user

app_name = 'myLibrary'

urlpatterns = [
    path("library/", show_library, name="show_library"),
    path("borrow-books/<int:book_id>", borrow_books, name="borrow_books"),
    path("get_borrowed_books_user/<int:user_id>", get_borrowed_books_user, name="get_borrowed_books_user"),
    path("get_favorite_books_user/<int:user_id>", get_favorite_books_user, name="get_favorite_books_user"),
]