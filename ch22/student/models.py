from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length = 75)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=70)
    roll = models.IntegerField()
    


# python manage.py makemigrations

# python manage.py migrate