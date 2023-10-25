from django.urls import path
from . import views

urlpatterns = [
    path('genre_grouping/', views.genre_grouping, name='genre_grouping'),
]
