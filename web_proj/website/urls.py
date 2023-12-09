from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('users', views.users, name="users"),
    path('rating', views.rating, name="rating"),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('logout', views.logout, name="logout")
]