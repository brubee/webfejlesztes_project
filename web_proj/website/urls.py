from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('users', views.users, name="users"),
    path('rating', views.rating, name="rating"),
    path('addUserTest', views.addUserTest, name="addUserTest"),
    path('addRatingTest', views.addRatingTest, name="addRatingTest")
]