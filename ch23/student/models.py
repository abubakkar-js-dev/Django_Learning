from django.db import models

# Create your models here.

class Profile(models.Model):
    name=models.CharField(max_length=75)
    email=models.EmailField(max_length=255)
    city=models.CharField(max_length=75)
    roll_number=models.IntegerField(max_length=25,default=0)
    grade=models.CharField(max_length=2,default="F")