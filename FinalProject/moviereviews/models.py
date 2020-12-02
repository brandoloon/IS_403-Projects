from django.db import models
from datetime import date
from django.contrib.auth.models import User
# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.FloatField()
    description = models.TextField()
    date = models.DateField(default=date.today())

    def __str__(self):
        return self.movie.__str__()


