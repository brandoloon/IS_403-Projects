from django.urls import path
from .views import LoginView, BrowseView, CreateProfileView, PersonalMovieView, ProfileSettingsView, CreateReviewView, SingleReviewView, FeedView

urlpatterns = [
    path('', LoginView, name = 'login'),
    path('browse/', BrowseView, name = 'browse'),
    path('new-user/', CreateProfileView, name = 'new-user'),
    path('profile/', PersonalMovieView, name = 'my-reviews'),
    path('profile/settings/', ProfileSettingsView, name = 'update-profile'),
    path('new-review/', CreateReviewView, name = 'new-review'),
    path('browse/<int:review_id>/', SingleReviewView, name = 'single-review'),
    path('feed/', FeedView, name = 'feed'),
]
