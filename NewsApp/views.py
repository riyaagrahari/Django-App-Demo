from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def News(request):
    return HttpResponse("<h1>Welcome to News Page</h1>")

def Home(request):
    return HttpResponse("<h1>Welcome to Home Page</h1>")

def Contact(request):
    return HttpResponse("<h1>Welcome to Contact Page</h1>")