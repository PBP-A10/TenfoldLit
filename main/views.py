from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from main.models import Book
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from django.http import HttpResponse
from django.core import serializers
from .models import Book
from django.db.models import Q

def show_home(request):
    return render(request, 'home.html')

def start_reading(request):
    return render(request, 'index.html')


#def get_books(request):
#    data = Book.objects.all()
#    serialized_data = serializers.serialize("json", data)
#    return HttpResponse(serialized_data, content_type='application/json') 

def get_books(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data),
                         content_type="application/json")

def get_filtered_books(request, genre):
    books = Book.objects.filter(genre__icontains=genre)
    data = serializers.serialize('json', books)
    return HttpResponse(data, content_type='application/json')

