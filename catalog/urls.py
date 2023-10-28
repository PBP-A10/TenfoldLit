from django.urls import path
from catalog.views import book_list, my_library, mark_as_favorite, add_review, book_reviews

urlpatterns = [
    path('book_list/', book_list, name='book_list'),
    path('my_library/', my_library, name='my_library'),
    path('mark_as_favorite/<int:book_id>/', mark_as_favorite, name='mark_as_favorite'),
    path('book_reviews/<int:book_id>/', book_reviews, name='book_reviews'),
    path('add_review/<int:book_id>/', add_review, name='add_review'),
]
