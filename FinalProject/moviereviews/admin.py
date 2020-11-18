from django.contrib import admin
from .models import Review, Movie

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['movie_title', 'user']
    def movie_title(self, obj):
        return obj.movie.title

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title',]
    
