from django.urls import path
from catalog.views import book_list, mark_as_favorite, add_review, book_reviews, my_favorites, ratings, get_reviews

app_name = 'catalog'

urlpatterns = [
    path('book_list/', book_list, name='book_list'),
    path('my_favorites/', my_favorites, name='my_library'),
    path('ratings/', ratings, name='ratings'),
    path('book_reviews/<int:book_id>/', book_reviews, name='book_reviews'),
    path('add_review/<int:book_id>/', add_review, name='add_review'),
    path('get_reviews/<int:book_id>/', get_reviews, name='get_reviews'),
    path('mark_as_favorite/<int:book_id>/', mark_as_favorite, name='mark_as_favorite'),
]
