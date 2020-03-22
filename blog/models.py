from django.db import models
from django.contrib.auth.models import User 

# Create your models here.




class WriteBlog(models.Model):
    title   = models.CharField(max_length=20)
    author  = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    content = models.TextField() 