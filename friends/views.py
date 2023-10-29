from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import UserConnections
from django.contrib.auth.models import User
from django.core import serializers
from friends.models import UserConnections

# Create your views here.

@login_required
def view_friends(request):
    user_connections, created = UserConnections.objects.get_or_create(user=request.user)
    friends = user_connections.get_friends()
    return render(request, 'friends.html', {'friends': friends, 'current_user': request.user})

@login_required
def follow_friend(request, friend_id):
    if request.method == 'POST':
        user_connections = UserConnections.objects.get(user=request.user)
        friend = UserConnections.objects.get(pk=friend_id)
        user_connections.add_friend(friend)
        return HttpResponse(b"FOLLOWED", status=201)
    return HttpResponseNotFound()

@login_required
def unfollow_friend(request, friend_id):
    if request.method == 'POST':
        user_connections = UserConnections.objects.get(user=request.user)
        friend = UserConnections.objects.get(pk=friend_id)
        user_connections.remove_friend(friend)
        return HttpResponse(b"UNFOLLOWED", status=201)
    return HttpResponseNotFound()

@login_required
def get_friends(request):
    user_connections = UserConnections.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', user_connections), content_type='application/json')

@login_required
def get_all_user_connections(request):
    users_connections = UserConnections.objects.all()
    return HttpResponse(serializers.serialize("json", users_connections), content_type="aplication/json")

def get_user(request, user_id):
    user = User.objects.filter(pk=user_id)
    return HttpResponse(serializers.serialize('json', user), content_type='application/json')

def get_user_connections(request, user_id):
    user = UserConnections.objects.filter(pk=user_id)
    return HttpResponse(serializers.serialize('json', user), content_type='application/json')