from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Title(models.Model):
    first_name = models.CharField(max_length=200)

class Text(models.model):
    text_field = models.TextField()


User=get_user_model()
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content= models.TextField()
    def __str__(self):
        return self.title

class Timefield(models.Model):
    time_field = models.DateTimeField()

import datetime
 

d = datetime.date(2022, 10, 19)
 

geek_object = models.Model.objects.create(geeks_field = d)
geek_object.save()