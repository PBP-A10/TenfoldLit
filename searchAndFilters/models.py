from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    writers = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    search_count = models.PositiveIntegerField(default=0)
