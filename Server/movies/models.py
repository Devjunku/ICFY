from django.conf import settings
from django.db import models

# Create your models here.

class Movie(models.Model):
    adult = models.BooleanField()
    # genre_id
    popularity = models.DecimalField(max_digits=20, decimal_places=10)
    title = models.CharField(max_length=100)
    overview = models.TextField()
    poster_path = models.TextField(null=True)
    vote_average = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.title