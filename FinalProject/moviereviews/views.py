from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def LoginView(request) :
    return render(request, 'moviereviews/login.html')

def BrowseView(request) :
    return render(request, 'moviereviews/browse.html')

def RegisterView(request) :
    return render(request, 'moviereviews/register.html')

def MyReviewsView(request) :
    return render(request, 'moviereviews/my_reviews.html')

def SettingsView(request) :
    return render(request, 'moviereviews/settings.html')

def NewReviewView(request) :
    return render(request, 'moviereviews/new_review.html')

def ReviewView(request) :
    return render(request, 'moviereviews/review.html')

