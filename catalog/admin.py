from django.contrib import admin
from .models import UserFavorite, UserReview

# Register the UserFavorite model
admin.site.register(UserFavorite)

# Register the UserReview model
admin.site.register(UserReview)
