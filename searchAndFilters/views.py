from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from main.models import Book
from django.http import HttpResponse
from django.core import serializers

def genre_grouping(request):
    books = Book.objects.all()
    genres = set([genre.strip() for book in books for genre in book.genre.split(',')])
    grouped_books = {}

    for genre in genres:
        grouped_books[genre] = books.filter(genre__icontains=genre)

    return render(request, 'genre_grouping.html', {'grouped_books': grouped_books})

def get_filtered_books(request, genre):
    books = Book.objects.filter(genre__icontains=genre)
    data = serializers.serialize('json', books)
    return HttpResponse(data, content_type='application/json')