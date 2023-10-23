from django.urls import path
from main.views import get_books

app_name = 'main'

urlpatterns = [
    path("", get_books, name="get_books"),
]