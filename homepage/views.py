from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from main.models import Book
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.db import transaction  # Impor modul transaction

from django.http import HttpResponse
from django.core import serializers
from .models import Book  # Pastikan Anda mengimpor model Book dari modul yang sesuai

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


