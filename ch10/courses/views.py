from django.shortcuts import render


# Create your views here.

def home(req):
    return render(req,'courses/courses.html')

def blogs(req):
    return render(req,'courses/blogs.html')