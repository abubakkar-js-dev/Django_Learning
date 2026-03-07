from django.db import models

# Create your models here.

class Profile(models.Model):
    name=models.CharField(max_length=75)
    roll=models.IntegerField()
    email=models.EmailField(max_length=255)
    city=models.CharField(max_length=75)
    state=models.CharField(max_length=75)

    def __str__(self):
        return self.name


class Result(models.Model):
    stu_id=models.ForeignKey(Profile,on_delete=models.CASCADE)
    email=models.EmailField(max_length=255)
    marks=models.IntegerField()

    def __str__(self):
        return self.email