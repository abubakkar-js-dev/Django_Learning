from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def courses(req):
    return HttpResponse('Here is your all courses')

def learn_python(req):
    return HttpResponse('<h3>All python tutorials here</h3>')

def learn_javascript(req):
    return HttpResponse('<h3>All Javascript tutorials here</h3>')
