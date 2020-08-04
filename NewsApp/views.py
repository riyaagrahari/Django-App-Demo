from django.shortcuts import render
from .models import News
# Create your views here.


def Home(request):

    context = {
        "name":"Riya Agrahari",
        "number": 7579290876
    }

    return render(request, 'home.html', context)


def NewsP(request):

    obj = News.objects.get(id=1)

    context = {
        "data": obj
    
    }
    return render(request, 'news.html', context)

def NewsDate(request, year):

    article_list = News.objects.filter(pub_date__year = year)


    context = {
        'year': year,
        'article_list': article_list
    }

    return render(request, 'newsdate.html', context)


def Contact(request):
    return render(request, 'contact.html')
