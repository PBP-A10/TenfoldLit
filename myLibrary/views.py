from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from catalog.models import UserFavorite
from main.models import Book
from myLibrary.models import BorrowedBooks


# Create your views here.
@login_required(login_url='/login')
def show_favorite(request):
    favorite_books = UserFavorite.objects.all()
    return HttpResponse(serializers.serialize("json", favorite_books), content_type="application/json")

@login_required(login_url='/login')
def show_library(request):
    borrowed_books = BorrowedBooks.objects.filter(user=request.user)
    return render(request, 'library.html', {'books': borrowed_books})

def get_borrowed_boks(request):
    borrowed_books = BorrowedBooks.objects.filter(user=request.user)
    serialized_books = [
        {
            'id': book.id,
            'title': book.book.title,
            'date_ended': book.date_ended  # Format the date as a string
        }
        for book in borrowed_books
    ]
    return JsonResponse(serialized_books, safe=False)

@csrf_exempt
def borrow_books(request, book_id):
    book = Book.objects.get(pk=book_id)
    user = request.user
    
    if request.method == 'POST':
        if BorrowedBooks.objects.filter(user=user, book=book).exists():
            return HttpResponse(b"tidak berhasil", status=400)

        # user = request.user
        date_borrowed = timezone.now()
        date_ended = request.POST.get("date_ended")
        
        borrowed_book = BorrowedBooks(user=user, book=book, date_borrowed=date_borrowed, date_ended=date_ended)
        borrowed_book.save()

        return HttpResponse(b"berhasil", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def return_book(request, book_id):
    if request.method == 'DELETE':
        try:
            book = BorrowedBooks.objects.get(pk=book_id)
            book.delete()
            return HttpResponse("Deleted", status=204)
        except BorrowedBooks.DoesNotExist:
            return HttpResponse("Borrowed book not found", status=404)

    return HttpResponse("Invalid request method", status=405)