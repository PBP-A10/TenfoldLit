from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title = models.TextField(null=True, blank=True)
    author = models.TextField(null=True, blank=True)
    bookformat = models.TextField(null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    img = models.URLField(null=True, blank=True)
    genre = models.TextField(null=True, blank=True)
    isbn = models.TextField(null=True, blank=True)
    isbn13 = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    reviews = models.IntegerField(null=True, blank=True)
    totalratings = models.IntegerField(null=True, blank=True)

class UserFavorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

class UserReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()