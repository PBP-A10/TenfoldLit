from django.db import models
from django.contrib.auth.models import User
from main.models import Book

# Create your models here.

class BorrowedBooks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_borrowed = models.DateField(auto_now_add=False)
    date_ended = models.DateField(auto_now_add=False)