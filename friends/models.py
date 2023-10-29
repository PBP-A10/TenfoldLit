from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserConnections(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField('self', blank=True, symmetrical=False)

    def add_friend(self, friend):
        self.friends.add(friend)

    def remove_friend(self, friend):
        self.friends.remove(friend)

    def get_friends(self):
        return self.friends.all()