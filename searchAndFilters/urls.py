from django.urls import path
from searchAndFilters.views import genre_grouping, get_filtered_books

app_name = 'searchAndFilters'

urlpatterns = [
    path('search/', genre_grouping, name='register'),
    path('get_filtered_books/<str:genre>', get_filtered_books, name='get-filtered-books'),
]