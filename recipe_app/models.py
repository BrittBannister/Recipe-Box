from django.db import models
from django.contrib.auth.models import User

'''
USER:
username
password
email

one to one
*********
AUTHOR:
name = charfield
bio = textfield

one to many
***********
RECIPE:
title = charfield
author = foreign key
description = textfield
time required = charfield (ex: one hour)
instructions = textfield
'''

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=150)
    user = models.OneToOneField(User, on_delete= models.CASCADE)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    time_required = models.CharField(max_length=100)
    instructions = models.TextField()

    def __str__(self):
        return f"{self.title} | {self.author}"
