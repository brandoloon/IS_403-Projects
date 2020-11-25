from django.contrib import admin
from .models import Review, Movie

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['movie', 'user']
    

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass
    
