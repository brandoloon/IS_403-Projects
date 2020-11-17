from django.db import models
from datetime import date

# Create your models here.
class Review(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    user = models.CharField(max_length=30)
    movie = models.CharField(max_length=50)
    rating = models.FloatField()
    description = models.TextField()
    date = models.DateField(default=date.today())

