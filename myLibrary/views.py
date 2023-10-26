from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.urls import reverse
from catalog.models import UserFavorite
from main.models import Book
from myLibrary.models import BorrowedBooks
from myLibrary.forms import UserBorrowForm

# Create your views here.
def show_favorite(request):
    favorite_books = UserFavorite.objects.all()
    return HttpResponse(serializers.serialize("json", favorite_books), content_type="application/json")

@login_required(login_url='/login')
def show_library(request):
    borrowed_books = BorrowedBooks.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", borrowed_books), content_type="application/json")

def borrow_books(request, book_id):
    book = Book.objects.get(pk=book_id)

    if request.method == 'POST':
        form = UserBorrowForm(request.POST)
        if form.is_valid():
            borrowed_book = form.save(commit=False)
            borrowed_book.user = request.user
            borrowed_book.book = book
            borrowed_book.date_borrowed = request.date_borrowed
            borrowed_book.date_ended = request.date_ended
            borrowed_book.save()

    context = {}
    return render(request, 'borrow_books.html', context)
