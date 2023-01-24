from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)

class Ratings(models.Model):
    movie = models.ForeignKey(Movie)
    user = models.ForeignKey(User)
