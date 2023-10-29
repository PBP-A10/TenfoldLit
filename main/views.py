from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from main.models import Book
from unicodedata import name
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
import requests


# Create your views here.
def get_books(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data),
                         content_type="application/json")

def get_book_json(request):
    books = Book.objects.all()
    return HttpResponse(serializers.serialize('json', books))

@login_required(login_url='/login')
def homepage(request):
    if 'last_login' not in request.COOKIES.keys():
        return redirect('auth_module:login')

    context = {
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "homepage.html", context)