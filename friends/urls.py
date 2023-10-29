from django.urls import path
from friends.views import view_friends, follow_friend, unfollow_friend, get_friends, get_users_connections

app_name = 'friends'

urlpatterns = [
    path('view_friends/', view_friends, name='view_friends'),
    path('follow_friend/<int:friend_id>/', follow_friend, name='follow_friend'),
    path('unfollow_friend/<int:friend_id>/', unfollow_friend, name='unfollow_friend'),
    path('get_friends/', get_friends, name='get_friends'),
    path('get_users_connections/', get_users_connections, name='get_users_connections'),
]