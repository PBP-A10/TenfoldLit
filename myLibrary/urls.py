from django.urls import path
from myLibrary.views import show_library, borrow_books

app_name = 'myLibrary'

urlpatterns = [
    path("library/", show_library, name="show_library"),
    path("borrow-books/<int:book_id>", borrow_books, name="borrow_books"),
]