from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def LoginView(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            return render(request, 'moviereviews/login.html')

    return render(request, 'moviereviews/login.html')

def BrowseView(request):
    return render(request, 'moviereviews/browse.html')

def RegisterView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            return render(request, 'moviereviews/register.html')

    return render(request, 'moviereviews/register.html')

def MyReviewsView(request):
    return render(request, 'moviereviews/my_reviews.html')

def SettingsView(request):
    if request.method == 'POST':
        request.user.first_name=request.POST['first_name']
        request.user.last_name=request.POST['last_name']
        request.user.email=request.POST['email']

    return render(request, 'moviereviews/settings.html')

def NewReviewView(request) :
    return render(request, 'moviereviews/new_review.html')

def ReviewView(request):
    return render(request, 'moviereviews/review.html')

