from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length = 75)
    email = models.EmailField(unique=True, max_length=255)
    city = models.CharField(max_length=70)
    roll = models.IntegerField()
    state = models.CharField(max_length=70)
    comment = models.CharField(max_length=70,default='This is default comment')

    


# python manage.py makemigrations

# python manage.py migrate

# python manage.py sqlmigrate student 0001