from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def LoginView(request) :
    return HttpResponse('Login Page')

def BrowseView(request) :
    return HttpResponse('Browse Page')

def CreateProfileView(request) :
    return HttpResponse('Create Profile Page')

def PersonalMovieView(request) :
    return HttpResponse('Personal Movie Page')

def ProfileSettingsView(request) :
    return HttpResponse('Profile Settings Page')

def CreateReviewView(request) :
    return HttpResponse('Create Review Page')

def SingleReviewView(request) :
    return HttpResponse('View Review Page')

def FeedView(request) :
    return HttpResponse('Review Feed Page')
