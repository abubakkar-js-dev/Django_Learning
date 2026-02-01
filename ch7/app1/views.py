from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello from home page")

def app1(requst):
    return HttpResponse("Hello from app1")

def app1_greet(request):
    return HttpResponse("Hey there, How are you?")
