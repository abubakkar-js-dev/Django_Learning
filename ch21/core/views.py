from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(req):
    return render(req,'core/home.html',content_type='text/html')


def about(req):
    return render(req,'core/about.html',content_type='text/html')
