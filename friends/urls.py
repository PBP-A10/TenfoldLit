from django.urls import path
from friends.views import view_friends, follow_friend, unfollow_friend, get_friends, get_all_user_connections, get_user, \
                        get_user_connections, get_friends_user_object, get_all_users,get_current_user, get_all_user_connections_object, \
                        follow_friend_flutter, unfollow_friend_flutter

app_name = 'friends'

urlpatterns = [
    path('view_friends/', view_friends, name='view_friends'),
    path('follow_friend/<int:friend_id>/', follow_friend, name='follow_friend'),
    path('unfollow_friend/<int:friend_id>/', unfollow_friend, name='unfollow_friend'),
    path('get_friends/', get_friends, name='get_friends'),
    path('get_all_user_connections/', get_all_user_connections, name='get_all_user_connections'),
    path('get_user/<int:user_id>', get_user, name='get_user'),
    path('get_user_connections/<int:user_id>', get_user_connections, name='get_user_connections'),
    path('get_friends_user_objects/<int:user_connection_id>', get_friends_user_object, name='get_friends_user_objects'),
    path('get_all_users/', get_all_users, name='get_all_users'),
    path('get_current_user/', get_current_user, name='get_current_user'),
    path('get_all_user_connections_object/', get_all_user_connections_object, name='get_all_user_connections_object'),
    path('follow_friend_flutter/<int:friend_id>/', follow_friend_flutter, name='follow_friend_flutter'),
    path('unfollow_friend_flutter/<int:friend_id>/', unfollow_friend_flutter, name='unfollow_friend_flutter'),
]