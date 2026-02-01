from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(req):
    return HttpResponse('<h4>Hello, this is home page! </h4>')

def category(req):
    return HttpResponse('This is category section in home page')