from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Rater, Rating
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home(request):
    return render(request, 'home.html')


@login_required(login_url='login')
def users(request):
    if request.GET.get('mode'):
        mode = request.GET['mode']
    else:
        mode = 'add'

    if request.method == 'POST' and 'createUser' in request.POST:
        if request.POST.get('name') == '' or \
                request.POST.get('age') == '':
            messages.error(request, "Please fill in the necessary information")
            return HttpResponseRedirect(reverse("users"))
        Rater.objects.create(name=request.POST.get('name'), age=request.POST.get('age'),
                             countryOfOrigin=request.POST.get('countryOfOrigin'))
        messages.success(request, "User created successfully")
    if request.method == 'POST' and 'editUser' in request.POST:
        if Rater.objects.filter(id=request.POST.get('id')).count() == 0:
            messages.error(request, "The User doesn't exist")
            return HttpResponseRedirect(reverse("users"))
        newName = request.POST.get('name')
        if newName == '':
            newName = Rater.objects.filter(id=request.POST.get('id'))[0].name
        newAge = request.POST.get('age')
        if newAge == '':
            newAge = Rater.objects.filter(id=request.POST.get('id'))[0].age
        newCOO = request.POST.get('countryOfOrigin')
        if newCOO == '':
            newCOO = Rater.objects.filter(id=request.POST.get('id'))[0].countryOfOrigin
        Rater.objects.filter(id=request.POST.get('id')).update(name=newName,
                                                               age=newAge,
                                                               countryOfOrigin=newCOO)
        messages.success(request, "User edited successfully")

    if request.method == 'POST' and 'deleteUser' in request.POST:
        Rater.objects.filter(id=request.POST.get('id')).delete()
        messages.success(request, "User deleted successfully")
    return render(request, 'users.html', {'data': Rater.objects.all(),
                                          'mode': mode})


@login_required(login_url='login')
def rating(request):
    if request.GET.get('mode'):
        mode = request.GET['mode']
    else:
        mode = 'add'

    if request.method == 'POST' and 'createRating' in request.POST:
        if request.POST.get('title') == '' or \
                request.POST.get('rating') == '':
            messages.error(request, "Please fill in the necessary information")
            return HttpResponseRedirect(reverse("rating"))
        if Rater.objects.filter(name=request.POST.get('rater')).count() == 0:
            messages.error(request, "This User doesn't exist")
            return HttpResponseRedirect(reverse("rating"))
        Rating.objects.create(rater=Rater.objects.filter(name=request.POST.get('rater'))[0],
                              title=request.POST.get('title'),
                              opinion=request.POST.get('opinion'),
                              rating=request.POST.get('rating'))
        messages.success(request, "Rating created successfully")
    if request.method == 'POST' and 'editRating' in request.POST:
        if Rating.objects.filter(id=request.POST.get('id')).count() == 0:
            messages.error(request, "The Rating doesn't exist")
            return HttpResponseRedirect(reverse("rating"))
        if request.POST.get('rater') == '' or Rater.objects.filter(name=request.POST.get('rater')).count() == 0:
            newUser = Rating.objects.filter(id=request.POST.get('id'))[0].rater
        else:
            newUser = Rater.objects.filter(name=request.POST.get('rater'))[0]
        newTitle = request.POST.get('title')
        if newTitle == '':
            newTitle = Rating.objects.filter(id=request.POST.get('id'))[0].title
        newOpinion = request.POST.get('opinion')
        if newOpinion == '':
            newOpinion = Rating.objects.filter(id=request.POST.get('id'))[0].opinion
        newRating = request.POST.get('rating')
        if newRating == '':
            newRating = Rating.objects.filter(id=request.POST.get('id'))[0].rating
        Rating.objects.filter(id=request.POST.get('id')).update(rater=newUser, title=newTitle, opinion=newOpinion,
                                                                rating=newRating)
        messages.success(request, "Rating edited successfully")

    if request.method == 'POST' and 'deleteRating' in request.POST:
        Rating.objects.filter(id=request.POST.get('id')).delete()
        messages.success(request, "Rating deleted successfully")
    return render(request, 'rating.html', {'data': Rating.objects.all(),
                                           'mode': mode})


def login(request):
    if request.method == 'POST' and 'login' in request.POST:
        user = authenticate(request,
                            username=request.POST.get('username'),
                            password=request.POST.get('password'))
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Successful log-in")
            return HttpResponseRedirect(reverse("home"))
        else:
            messages.error(request, "Wrong log-in credentials")
            return HttpResponseRedirect(reverse("login"))
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST' and 'register' in request.POST:
        if User.objects.filter(username=request.POST.get('username')).exists():
            messages.error(request, "Username already taken")
            return HttpResponseRedirect(reverse("register"))
        if request.POST.get('username') == '' or \
                request.POST.get('password') == '' or \
                request.POST.get('repassword') == '' or \
                request.POST.get('email') == '':
            messages.error(request, "Please fill in the necessary fields")
            return HttpResponseRedirect(reverse("register"))
        if request.POST.get('password') != request.POST.get('repassword'):
            messages.error(request, "The passwords do not match")
            return HttpResponseRedirect(reverse("register"))
        user = User.objects.create_user(request.POST.get('username'),
                                        request.POST.get('email'),
                                        request.POST.get('password'))
        user.save()
        messages.success(request, "Successful registration")
    return render(request, 'register.html')


def logout(request):
    auth_logout(request)
    messages.success(request, "Successful log-out")
    return HttpResponseRedirect(reverse("home"))
