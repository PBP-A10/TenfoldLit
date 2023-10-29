from django.urls import path
from profile_user.views import get_user_data, update_profile

urlpatterns = [
    path('profile_user/', get_user_data, name='get_user_data'),
    path('update_profile/', update_profile, name='update_profile'),
    # Other URL patterns for your app
]
