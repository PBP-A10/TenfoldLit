from django.urls import path
from .views import show_home, start_reading, get_books
from . import views


app_name = 'main'

urlpatterns = [
    path('', show_home, name='show_home'),
    #path("books/<slug:val>", views.GenreView.as_view(), name='books'),
    path('start-reading/', start_reading, name='start_reading'),
    path('get-books', get_books, name = 'get_books'),
    path("", get_books, name="get_books"),
    ]