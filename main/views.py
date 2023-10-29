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
from main.models import Book
from unicodedata import name
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
import requests

def show_home(request):
    return render(request, 'home.html')

def start_reading(request):
    return render(request, 'index.html')


def get_books(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data),
                         content_type="application/json")

def Home(request):
    return render(request, 'index.html')

def Register(request):
    if request.method =='POST' :
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2 :
            messages.error(request, 'Passwords salah! Coba Lagi!')
            return redirect('Register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username sudah digunakan!')
            return redirect('Register')
        
        if User.objects.filter(email=email).exists():
            messages.error(requests,'Email sudah digunakan!')
            return redirect('Register')
        
        user = User.objects.create_user(username=username, email=email)
        user.set_password(password1)
        user.save()

        messages.success(request, 'Registrasi berhasil!')
        return redirect('Register')
    
    return render(request, 'Register.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username)

def Logout(request):
    logout(request)
    messages.sucess(request, 'Berhasil Log Out')
     
    return redirect('index.html')

#def Recomendation(request): 
    

