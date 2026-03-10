from django.db import models

# Create your models here.

GENDER = [
    ("M", "Male"),
    ("F", "Female"),
]

class Student(models.Model):

    student_id = models.IntegerField(primary_key = True,null=False)
    name = models.CharField(max_length = 100,null = False,blank = False, help_text='Enter full name')
    email = models.EmailField(unique = True)
    phone =  models.CharField(null=False)
    age = models.IntegerField(default = 18)
    gender = models.CharField(max_length=1,choices=GENDER)
    bio = models.TextField(null = True,blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta: 
        ordering= ['-name']
        unique_together = ['email', 'phone']
        verbose_name = 'Student'
        verbose_name_plural = 'Students'






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