from django.urls import path
from searchAndFilters.views import genre_grouping, get_filtered_books, search_books, get_search_books


urlpatterns = [
    path('search/', genre_grouping, name='genre-grouping'),
    path('get_filtered_books/<str:genre>', get_filtered_books, name='get-filtered-books'),
    path('search_books/', search_books, name='search_books'),
    path('get_search_books/<str:search_query>', get_search_books, name='get_search_books'),
]