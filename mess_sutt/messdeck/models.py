from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

from django.db import models
from django import forms
import datetime


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bits_id = models.CharField(max_length=20, blank=False)
    mess = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.user.username

class Date(models.Model):
    date = models.DateField(unique=True)

class breakfast(models.Model):
    date = models.ForeignKey(Date, on_delete=models.CASCADE)
    stars = models.IntegerField(default=0)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class lunch(models.Model):
    date = models.ForeignKey(Date, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
        
class dinner(models.Model):
    date = models.ForeignKey(Date, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='feedback_complaints/')

# class Rating(models.Model):
#     meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
#     stars = models.IntegerField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE)


class attend(models.Model):
    has_attended_breakfast = models.BooleanField(default=False)
    has_attended_lunch = models.BooleanField(default=False)
    has_attended_dinner = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.ForeignKey(Date, on_delete=models.CASCADE,null=True)