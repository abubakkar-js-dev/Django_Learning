from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blogs(req):
    return HttpResponse('This is blogs')

def single_blog(req):
    return HttpResponse('This is single blogs')

