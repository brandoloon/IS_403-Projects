from django.urls import path
from .views import LoginView, BrowseView, RegisterView, MyReviewsView, SettingsView, NewReviewView, ReviewView

urlpatterns = [
    path('', LoginView, name = 'login'),
    path('browse/', BrowseView, name = 'browse'),
    path('register/', RegisterView, name = 'register'),
    path('profile/', MyReviewsView, name = 'my-reviews'),
    path('profile/settings/', SettingsView, name = 'settings'),
    path('new-review/', NewReviewView, name = 'new-review'),
    path('browse/<int:review_id>/', ReviewView, name = 'review'),
]
