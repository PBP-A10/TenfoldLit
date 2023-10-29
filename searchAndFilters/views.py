from django.shortcuts import render
from main.models import Book
from django.http import HttpResponse
from django.core import serializers
from django.db.models import Q

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

def get_search_books(request, search_query):
    books = Book.objects.filter(Q(title__icontains=search_query) | Q(author__icontains=search_query))
    data = serializers.serialize('json', books)
    return HttpResponse(data, content_type='application/json')

def search_books(request):
    book = Book.objects.all()
    return render(request, 'genre_grouping.html', {'books' : book})

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