import json
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import UserConnections
from django.contrib.auth.models import User
from django.core import serializers
from friends.models import UserConnections
from django.views.decorators.csrf import csrf_exempt

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
@csrf_exempt
def follow_friend_flutter(request, friend_id):
    if request.method == 'POST':
        user_connections = UserConnections.objects.get(user=request.user)
        friend = UserConnections.objects.get(pk=friend_id)
        user_connections.add_friend(friend)
        
        response_data = {"status": "success", "message": "User followed successfully"}
        return JsonResponse(response_data, status=201)
    return HttpResponseNotFound()

@login_required
@csrf_exempt
def unfollow_friend_flutter(request, friend_id):
    if request.method == 'POST':
        user_connections = UserConnections.objects.get(user=request.user)
        friend = UserConnections.objects.get(pk=friend_id)
        user_connections.remove_friend(friend)

        response_data = {"status": "success", "message": "User unfollowed successfully"}
        return JsonResponse(response_data, status=201)
    return HttpResponseNotFound()

@login_required
def unfollow_friend(request, friend_id):
    if request.method == 'POST':
        user_connections = UserConnections.objects.get(user=request.user)
        friend = UserConnections.objects.get(pk=friend_id)
        user_connections.remove_friend(friend)

        response_data = {"status": "success", "message": "User unfollowed successfully"}
        return JsonResponse(response_data, status=201)
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

@login_required
def get_user_connections(request, user_id):
    user = UserConnections.objects.filter(pk=user_id)
    return HttpResponse(serializers.serialize('json', user), content_type='application/json')

@login_required
def get_friends_user_object(request, user_connection_id):
    connection = UserConnections.objects.get(pk=user_connection_id)
    friends = connection.get_friends()
    
    user_list = [
        {
            "user_connection_id": entry.pk,
            "user_id": entry.user.pk,
            "password": entry.user.password,
            "last_login": entry.user.last_login,
            "username": entry.user.username,
            "email": entry.user.email,
        }
        for entry in friends
    ]

    return JsonResponse(user_list, safe=False)

@login_required
def get_all_users(request):
    users = User.objects.all()

    user_list = [
        {
            "id": user.pk,
            "password": user.password,
            "last_login": user.last_login,
            "username": user.username,
            "email": user.email,
        }
        for user in users
    ]

    return JsonResponse(user_list, safe=False)

@login_required
def get_current_user(request):
    user_connection = UserConnections.objects.get(user=request.user)
    user_list = [
        {
            "user_connection_id": user_connection.pk,
            "user_id": request.user.id,
            "password": request.user.password,
            "last_login": request.user.last_login,
            "username": request.user.username,
            "email": request.user.email,
        }
    ]

    return JsonResponse(user_list, safe=False)

@login_required
def get_all_user_connections_object(request):
    connections = UserConnections.objects.all()

    user_list = [
        {
            "user_connection_id": entry.pk,
            "user_id": entry.user.pk,
            "password": entry.user.password,
            "last_login": entry.user.last_login,
            "username": entry.user.username,
            "email": entry.user.email,
        }
        for entry in connections
    ]

    return JsonResponse(user_list, safe=False)