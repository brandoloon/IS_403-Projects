from django.db import models
from datetime import date
from django.contrib.auth.models import User
# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=50)
class Review(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    movie = models.ForeignKey(Movie, models.CASCADE)
    rating = models.FloatField()
    description = models.TextField()
    date = models.DateField(default=date.today())


