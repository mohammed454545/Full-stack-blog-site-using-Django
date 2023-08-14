from django.db import models
from django.contrib.auth.models import User
from corse.models import Corses

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=100)
    img=models.ImageField()
    age=models.IntegerField()
    job=models.CharField(max_length=60)
    def __str__(self):
        return self.full_name


# Create your models here.
