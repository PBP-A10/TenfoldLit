import json
from django.shortcuts import render

# Create your views here.

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
    # print(request.user.id)
    borrowed_books = BorrowedBooks.objects.filter(user=request.user)
    serialized_books = [
        {
            'id': book.pk,
            'title': book.book.title,
            'date_ended': book.date_ended,  # Format the date as a string
            'book_image': book.book.img
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
def borrow_books_flutter(request, book_id):
    book = Book.objects.get(pk=book_id)
    user = request.user
    
    if request.method == 'POST':
        if BorrowedBooks.objects.filter(user=user, book=book).exists():
            return JsonResponse({"status": "failed"}, status=200)

        # user = request.user
        date_borrowed = timezone.now()

        data = json.loads(request.body)
        date_ended = data.get("date_ended")
        
        borrowed_book = BorrowedBooks(user=user, book=book, date_borrowed=date_borrowed, date_ended=date_ended)
        borrowed_book.save()

        return JsonResponse({"status": "success"}, status=200)

    return HttpResponseNotFound()

@csrf_exempt
def return_book(request, book_id):
    if request.method == 'POST':
        book = BorrowedBooks.objects.get(pk=book_id)
        book.delete()
        return JsonResponse({"message": "Deleted"}, status=200)

    # return HttpResponse("Invalid request method", status=405)

@csrf_exempt    
def return_damaged_book(request, book_id):
    if request.method == 'POST':
        borrowedBook = BorrowedBooks.objects.get(pk=book_id)
        book = Book.objects.get(pk=book_id)
        borrowedBook.delete()

        book.status = True
        book.save()

        return JsonResponse({"message": "Deleted"}, status=200)

    # return HttpResponse("Invalid request method", status=405)
    # context = {}
    # return render(request, 'borrow_books.html', context)

@login_required(login_url='/login')
def get_borrowed_books(request, user_id):
    borrowed_books = BorrowedBooks.objects.filter(pk=user_id)
    return HttpResponse(serializers.serialize("json", borrowed_books), content_type="application/json")

@login_required(login_url='/login')
def get_favorite_books(request, user_id):
    favorite_books = UserFavorite.objects.filter(pk=user_id)
    return HttpResponse(serializers.serialize("json", favorite_books), content_type="application/json")