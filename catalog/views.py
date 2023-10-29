from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import render, redirect
from main.models import Book
from catalog.models import UserFavorite, UserReview
from catalog.forms import UserReviewForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

@login_required
def my_favorites(request):
    user_favorites = UserFavorite.objects.filter(user=request.user)
    books = [favorite.book for favorite in user_favorites]
    return render(request, 'my_favorites.html', {'books': books})

@login_required
def mark_as_favorite(request, book_id):
    book = Book.objects.get(pk=book_id)
    user = request.user

    # Cek apakah buku ini sudah menjadi favorit pengguna
    is_favorite = UserFavorite.objects.filter(user=user, book=book).exists()

    if is_favorite:
        # Jika sudah menjadi favorit, hapus dari favorit
        UserFavorite.objects.filter(user=user, book=book).delete()
        is_favorite = False
    else:
        # Jika belum menjadi favorit, tambahkan ke favorit
        UserFavorite.objects.create(user=user, book=book)
        is_favorite = True

    # Kirim respons JSON yang berisi status favorit
    return JsonResponse({'is_favorite': is_favorite})

@login_required
def book_reviews(request, book_id):
    book = Book.objects.get(pk=book_id)
    reviews = UserReview.objects.filter(book=book)
    return render(request, 'book_detail.html', {'book': book, 'reviews': reviews})

def ratings(request):
    books = Book.objects.all().order_by('-user_avg_rating')
    return render(request, 'ratings.html', {'books': books})

def calculate_user_avg_rating(book):
    user_reviews = UserReview.objects.filter(book=book)
    total_reviews = user_reviews.count()

    if total_reviews > 0:
        total_user_rating = sum(review.rating for review in user_reviews)
        book.user_avg_rating = total_user_rating / total_reviews
    else:
        book.user_avg_rating = None

    book.save()

@csrf_exempt
def add_review(request, book_id):
    book = Book.objects.get(pk=book_id)
    user = request.user

    if request.method == 'POST':
        comment = request.POST.get("comment")
        rating = request.POST.get("rating")

        new_review = UserReview(user=user, book=book, rating=rating, comment=comment)
        new_review.save()

        return HttpResponse(b"berhasil", status=201)
    
    return HttpResponseNotFound()
    # return render(request, 'book_detail.html', {'book': book, 'form': form})

def get_reviews(request, book_id):
    reviews = UserReview.objects.filter(book_id=book_id)

    # Format data ulasan dalam format JSON
    reviews_data = [{'user': review.user.username, 'comment': review.comment} for review in reviews]

    return JsonResponse(reviews_data, safe=False)