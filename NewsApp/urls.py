from django.urls import path
from .views import NewsP, Home, Contact, NewsDate, register, addUser

urlpatterns = [
    path('', Home, name='home'),
    path('news/', NewsP, name='news'),
    path('newsdate/<int:year>', NewsDate, name='newsdate'),
    path('contact/', Contact, name='contact'),
    path('signup/', register, name='register'),
    path('addUser/', addUser, name='addUser'),


]