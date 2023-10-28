from django.db import models

# Create your models here.

GENRE_CHOICES =(('NOM', 'Nonfiction'),
                 ('HIS', 'History'), 
                 ('GAM', 'Games'), 
                 ('ESO', 'Esoterica'),
                 ('POE', 'Poetry'), 
                 ('CUL', 'Cultural'), 
                 ('REL', 'Religion'), 
                 ('ROM', 'Romance'), 
                 ('PRA', 'Prayer'), 
                 ('HTY', 'History'), 
                 ('CHE', 'Chess'), 
                 ('ATG', 'Astrology'), 
                 ('CAN', 'Canada'), 
                 ('SEQ', 'Sequential'), 
                 ('THE','Theology'), 
                 ('CTN', 'Christian'), 
                 ('EVG', 'Evangelism'), 
                 ('CTY', "Christianity"), 
                 ('SCE', 'Science'), 
                 ('BFY', 'Biography'), 
                 ('MLT', 'Military'))

class Genre(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.TextField(null=True, blank=True)
    author = models.TextField(null=True, blank=True)
    bookformat = models.TextField(null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    img = models.URLField(null=True, blank=True)
    genre = models.TextField(choices=GENRE_CHOICES, max_length=3,  default='NOM')
    isbn = models.TextField(null=True, blank=True)
    isbn13 = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    reviews = models.IntegerField(null=True, blank=True)
    totalratings = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.title