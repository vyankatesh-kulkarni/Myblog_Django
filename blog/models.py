from django.db import models
from django.contrib.auth.models import User 
from django import forms
# Create your models here.




 
class Category(models.Model):
    cname = models.CharField(max_length=30, primary_key=True) 

    def __str__(self):
        return self.cname



class WriteBlog(models.Model):
    title   = models.CharField(max_length=40)
    author  = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category,on_delete = models.CASCADE,default='others')
    content = models.TextField()


class SideWidget(models.Model):
    user    = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.TextField()

    
        