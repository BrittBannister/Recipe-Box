from django.db import models
'''
AUTHOR:
name = charfield
bio = textfield

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

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    time_required = models.CharField(max_length=100)
    instructions = models.TextField()
