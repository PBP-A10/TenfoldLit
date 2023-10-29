from django.urls import path
from main.views import get_books, homepage

app_name = 'main'

urlpatterns = [
    path("", homepage, name="homepage"),
]