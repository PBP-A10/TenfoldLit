from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('book_list/', views.book_list, name='book_list'),
    path('my_favorites/', views.my_favorites, name='my_library'),
    path('ratings/', views.ratings, name='ratings'),
    path('book_reviews/<int:book_id>/', views.book_reviews, name='book_reviews'),
    path('add_review/<int:book_id>/', views.add_review, name='add_review'),
    path('get_reviews/<int:book_id>/', views.get_reviews, name='get_reviews'),
    path('mark_as_favorite/<int:book_id>/', views.mark_as_favorite, name='mark_as_favorite'),
]