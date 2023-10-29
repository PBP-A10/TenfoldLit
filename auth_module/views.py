import datetime
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from friends.models import UserConnections
from auth_module.forms import RegisterUserForm


# Create your views here.
def register(request):
    form = RegisterUserForm()

    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user_connections, created = UserConnections.objects.get_or_create(user=user)
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:homepage')
            
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            response = HttpResponseRedirect(reverse("catalog:book_list")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:show_home'))
    response.delete_cookie('last_login')
    return response