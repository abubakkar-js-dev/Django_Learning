from django.shortcuts import render

# Create your views here.

def learn_django(req):
    return render(req,'course/django.html',{"name": "Django 6.0"},content_type='text/html')

def learn_python(req):
    return render(req,'course/python.html',content_type='text/html')