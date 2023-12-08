from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import User, Rating


def home(request):
    return render(request, 'home.html')


def users(request):
    if request.method == 'POST' and 'createUser' in request.POST:
        User.objects.create(name=request.POST.get('name'), age=request.POST.get('age'),
                            countryOfOrigin=request.POST.get('countryOfOrigin'))
        return HttpResponseRedirect(reverse("users"))
    return render(request, 'users.html', {'data': User.objects.all()})


def rating(request):
    if request.method == 'POST' and 'createRating' in request.POST:
        if User.objects.filter(id=request.POST.get('user')).count() == 0:
            print("User doesn't exist")
            return HttpResponseRedirect(reverse("rating"))
        Rating.objects.create(userId=User.objects.filter(id=request.POST.get('userId'))[0],
                              title=request.POST.get('title'),
                              opinion=request.POST.get('opinion'),
                              rating=request.POST.get('rating'))
        return HttpResponseRedirect(reverse("rating"))
    return render(request, 'rating.html', {'data': Rating.objects.all()})


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
