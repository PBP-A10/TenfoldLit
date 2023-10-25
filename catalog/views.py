from django.shortcuts import render, redirect
from catalog.models import Book, UserFavorite, UserReview
from catalog.forms import UserReviewForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'catalog/book_list.html', {'books': books})

def my_library(request):
    user_favorites = UserFavorite.objects.filter(user=request.user)
    books = [favorite.book for favorite in user_favorites]
    return render(request, 'catalog/my_library.html', {'books': books})

def mark_as_favorite(request, book_id):
    book = Book.objects.get(pk=book_id)
    user_favorite, created = UserFavorite.objects.get_or_create(user=request.user, book=book)
    return redirect('book_list')

def book_reviews(request, book_id):
    book = Book.objects.get(pk=book_id)
    reviews = UserReview.objects.filter(book=book)
    return render(request, 'catalog/book_reviews.html', {'book': book, 'reviews': reviews})

def add_review(request, book_id):
    book = Book.objects.get(pk=book_id)

    if request.method == 'POST':
        form = UserReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.book = book
            review.save()
            return redirect('book_reviews', book_id=book_id)
    else:
        form = UserReviewForm()

    return render(request, 'catalog/add_review.html', {'book': book, 'form': form})