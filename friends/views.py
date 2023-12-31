import json
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from catalog.models import UserFavorite
from myLibrary.models import BorrowedBooks
from profile_user.models import UserProfile
from .models import UserConnections
from django.contrib.auth.models import User
from django.core import serializers
from friends.models import UserConnections
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize

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

@login_required
def get_borrowed_books_user(request, user_id):
    current_user = User.objects.get(pk=user_id)
    borrowed_books = BorrowedBooks.objects.filter(user=current_user)
    serialized_books = [
        {
            'id': book.pk,
            'title': book.book.title,
            'date_ended': "2023-12-31",  # Format the date as a string
            'book_image': book.book.img,
            "author": book.book.author,
            "bookformat": book.book.bookformat,
            "desc": book.book.desc,
            "genre": book.book.genre,
            "isbn": book.book.isbn,
            "isbn13": book.book.isbn13,
            "link": book.book.link,
            "pages": book.book.pages,
            "rating": book.book.rating,
            "reviews": book.book.reviews,
            "totalratings": book.book.totalratings
        }
        for book in borrowed_books
    ]
    return JsonResponse(serialized_books, safe=False)

@login_required
def get_favorite_books_user(request, user_id):
    current_user = User.objects.get(pk=user_id)
    favorite_books = UserFavorite.objects.filter(user=current_user)
    serialized_books = [
        {
            'id': book.pk,
            'title': book.book.title,
            'date_ended': "2023-12-31",  # Format the date as a string
            'book_image': book.book.img,
            "author": book.book.author,
            "bookformat": book.book.bookformat,
            "desc": book.book.desc,
            "genre": book.book.genre,
            "isbn": book.book.isbn,
            "isbn13": book.book.isbn13,
            "link": book.book.link,
            "pages": book.book.pages,
            "rating": book.book.rating,
            "reviews": book.book.reviews,
            "totalratings": book.book.totalratings
        } for book in favorite_books
    ]
    return JsonResponse(serialized_books, safe=False)

@login_required
def get_user_profile(request, user_id):
    current_user = User.objects.get(pk=user_id)
    user_profile = UserProfile.objects.get(user=current_user)
    profile = [
        {
            'username': request.user.username,
            'profile': user_profile.profile_picture.url if user_profile.profile_picture else None
        }
    ]
    return JsonResponse(profile, safe=False)