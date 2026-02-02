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
def learn_django(req):
    date = datetime.datetime.now()
    return render(req,'course/django.html',{'dt': date})