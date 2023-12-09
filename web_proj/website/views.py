from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import User, Rating


def home(request):
    return render(request, 'home.html')


def users(request):
    if request.GET.get('mode'):
        mode = request.GET['mode']
    else:
        mode = 'add'

    if request.method == 'POST' and 'createUser' in request.POST:
        User.objects.create(name=request.POST.get('name'), age=request.POST.get('age'),
                            countryOfOrigin=request.POST.get('countryOfOrigin'))
    if request.method == 'POST' and 'editUser' in request.POST:
        if User.objects.filter(id=request.POST.get('id')).count() == 0:
            print("House does not exist")
            return HttpResponseRedirect(reverse("users"))
        newName = request.POST.get('name')
        if newName == '':
            newName = User.objects.filter(id=request.POST.get('id'))[0].name
        newAge = request.POST.get('age')
        if newAge == '':
            newAge = User.objects.filter(id=request.POST.get('id'))[0].age
        newCOO = request.POST.get('countryOfOrigin')
        if newCOO == '':
            newCOO = User.objects.filter(id=request.POST.get('id'))[0].countryOfOrigin
        User.objects.filter(id=request.POST.get('id')).update(name=newName, age=newAge, countryOfOrigin=newCOO)

    if request.method == 'POST' and 'deleteUser' in request.POST:
        User.objects.filter(id=request.POST.get('id')).delete()
    return render(request, 'users.html', {'data': User.objects.all(),
                                          'mode': mode})


def rating(request):
    if request.method == 'POST' and 'createRating' in request.POST:
        Rating.objects.create(user=User.objects.filter(name=request.POST.get('user'))[0],
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
