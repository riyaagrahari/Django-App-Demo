from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.


def Home(request):

    context = {
        "name":"Riya Agrahari",
        "number": 75792
    }

    return render(request, 'home.html', context)


def News(request):

    context = {
        "list":["Python", "Java", "C++", "C#", "Kotlin", "Ruby"],
        "mynum": 40
    }
    return render(request, 'news.html', context)

   


def Contact(request):
    return render(request, 'contact.html')