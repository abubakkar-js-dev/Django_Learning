from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def home(req):
    return HttpResponse("This is home page")

# example 1.0 variable template
# def learn_django(req):
#     return render(req,'course/django.html',{'cname': 'django 5.0 mastery'})


# example 1.1 variable template
# def learn_django(req):
#     cname = 'Django 5.0 mastery'
#     duration = '44 hours'
#     seats = 122
#     description = "Django is a high performance Full stack Web Framework for python"
#     couse_details = {
#         'cname': cname,
#         'duration': duration,
#         'seats': seats,
#         'description': description
#     }
#     return render(req,'course/django.html',couse_details)

# example 1.2 Date
# def learn_django(req):
#     date = datetime.datetime.now()
#     return render(req,'course/django.html',{'dt': date})


# example 2 float format
# def learn_django(req):
#     nums = {'v1': 96.278, 'v2': 96.000, 'v3': 96.3700}
#     return render(req,'course/django.html',nums)

# # example 3 If else

# def learn_django(req):
#     info = {'name': 'Django', 'version': '3.5','available': True}
#     return render(req,'course/django.html',info)

# # example 4 for loop and for loop counter

def learn_django(req):
    courses = [
        {"name": "Django Basics", "duration": "3 weeks", "level": "Beginner"},
        {"name": "Advanced Django", "duration": "6 weeks", "level": "Intermediate"},
        {"name": "REST APIs with DRF", "duration": "4 weeks", "level": "Intermediate"},
        {"name": "Full-Stack with Django & React", "duration": "8 weeks", "level": "Advanced"},
    ]
        


    return render(req,'course/django.html',{'courses': courses})