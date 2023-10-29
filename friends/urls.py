from django.urls import path
from friends.views import view_friends, follow_friend, unfollow_friend, get_friends, get_all_user_connections, get_user, get_user_connections

app_name = 'friends'

urlpatterns = [
    path('view_friends/', view_friends, name='view_friends'),
    path('follow_friend/<int:friend_id>/', follow_friend, name='follow_friend'),
    path('unfollow_friend/<int:friend_id>/', unfollow_friend, name='unfollow_friend'),
    path('get_friends/', get_friends, name='get_friends'),
    path('get_all_user_connections/', get_all_user_connections, name='get_all_user_connections'),
    path('get_user/<int:user_id>', get_user, name='get_user'),
    path('get_user_connections/<int:user_id>', get_user_connections, name='get_user_connections'),
]