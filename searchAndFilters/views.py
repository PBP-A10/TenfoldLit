from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView

from main import models
from .models import Filters

class BookSortView(ListView):
    model = Filters
    template_name = 'bookstore/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        query = self.request.GET.get('q')
        order = self.request.GET.get('order')

        if query:
            # Search by title, genre, and writers
            queryset = Filters.objects.filter(
                Q(title__icontains=query) | 
                Q(genre__icontains=query) | 
                Q(writers__icontains=query)
            )
            queryset.update(search_count=models.F('search_count') + 1)
        else:
            queryset = Filters.objects.all()

        if order == 'rating':
            queryset = queryset.order_by('-rating')
        elif order == 'newest':
            queryset = queryset.order_by('id') 
        elif order == 'most_search':
            queryset = queryset.order_by('-search_count')

        return queryset
