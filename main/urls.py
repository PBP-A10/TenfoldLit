from django.urls import path
from main.views import show_home, start_reading, get_books
from . import views
from django.urls import path
# from auth_module.views import check_login_status  # Gantilah dengan import yang sesuai

app_name = 'main'

urlpatterns = [
    path('', show_home, name='show_home'),
    #path("books/<slug:val>", views.GenreView.as_view(), name='books'),
    path('start-reading/', start_reading, name='start_reading'),
    path('get-books', get_books, name = 'get_books'),
    path("", get_books, name="get_books"),
    # path('check-login-status/', check_login_status, name='check_login_status'),
]
