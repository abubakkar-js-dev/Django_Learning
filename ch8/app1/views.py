from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(req):
    return HttpResponse('Home page')

def learn_python(req,**kwargs):
    status = kwargs.get('status','Not allowed')
    print(status)
    return  HttpResponse(f'<h3>Hello Django {status}</h3>')

