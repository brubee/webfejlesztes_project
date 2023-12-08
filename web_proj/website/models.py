from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=50)
    age = models.IntegerField()
    countryOfOrigin = models.TextField(max_length=100)


class Rating(models.Model):
    id = models.AutoField(primary_key=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=100)
    opinion = models.TextField(max_length=1000)
    rating = models.FloatField()

