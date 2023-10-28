from django.urls import path
from . import views

urlpatterns = [
    path('book_list/', views.book_list, name='book_list'),
    path('my_library/', views.my_library, name='my_library'),
    path('mark_as_favorite/<int:book_id>/', views.mark_as_favorite, name='mark_as_favorite'),
    path('book_reviews/<int:book_id>/', views.book_reviews, name='book_reviews'),
    path('add_review/<int:book_id>/', views.add_review, name='add_review'),
]
