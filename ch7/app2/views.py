from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def app2(request):
    return HttpResponse("Hello from app-2")

def app2_greet(request):
    return HttpResponse('Hey how are you? you are using app2')