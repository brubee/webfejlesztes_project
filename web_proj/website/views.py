from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import User, Rating

# Create your views here.


def home(request):
    return render(request, 'home.html')


def users(request):
    return render(request, 'users.html')


def rating(request):
    return render(request, 'rating.html')


def addUserTest(request):
    User.objects.create(name='Test Name',
                        age=20,
                        countryOfOrigin='Canada')
    return HttpResponseRedirect(reverse("users"))


def addRatingTest(request):
    Rating.objects.create(userId=User(id=1),
                          title='The Big Test',
                          opinion="It wasn't the best...",
                          rating=3.7)
    return HttpResponseRedirect(reverse("rating"))


