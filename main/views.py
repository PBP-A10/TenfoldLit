from django.shortcuts import render
from .models import Book

def genre_grouping(request):
    books = Book.objects.all()
    genres = set([genre.strip() for book in books for genre in book.genre.split(',')])
    grouped_books = {}

    for genre in genres:
        grouped_books[genre] = books.filter(genre__icontains=genre)

    return render(request, 'genre_grouping.html', {'grouped_books': grouped_books})
