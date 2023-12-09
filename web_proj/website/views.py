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
    if request.GET.get('mode'):
        mode = request.GET['mode']
    else:
        mode = 'add'

    if request.method == 'POST' and 'createRating' in request.POST:
        Rating.objects.create(user=User.objects.filter(name=request.POST.get('user'))[0],
                              title=request.POST.get('title'),
                              opinion=request.POST.get('opinion'),
                              rating=request.POST.get('rating'))
    if request.method == 'POST' and 'editRating' in request.POST:
        if Rating.objects.filter(id=request.POST.get('id')).count() == 0:
            print("Rating doesn't exist")
            return HttpResponseRedirect(reverse("rating"))
        if request.POST.get('user') == '' or User.objects.filter(id=request.POST.get('user')).count() == 0:
            newUser = Rating.objects.filter(id=request.POST.get('id'))[0].user
        else:
            newUser = User.objects.filter(id=request.POST.get('user'))[0]
        newTitle = request.POST.get('title')
        if newTitle == '':
            newTitle = Rating.objects.filter(id=request.POST.get('id'))[0].title
        newOpinion = request.POST.get('opinion')
        if newOpinion == '':
            newOpinion = Rating.objects.filter(id=request.POST.get('id'))[0].opinion
        newRating = request.POST.get('rating')
        if newRating == '':
            newRating = Rating.objects.filter(id=request.POST.get('id'))[0].rating
        Rating.objects.filter(id=request.POST.get('id')).update(user=newUser, title=newTitle, opinion=newOpinion, rating=newRating)

    if request.method == 'POST' and 'deleteRating' in request.POST:
        Rating.objects.filter(id=request.POST.get('id')).delete()
    return render(request, 'rating.html', {'data': Rating.objects.all(),
                                           'mode': mode})
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
