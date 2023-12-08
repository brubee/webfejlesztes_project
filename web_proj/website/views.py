from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home.html')


def users(request):
    return render(request, 'users.html')


def rating(request):
    return render(request, 'rating.html')