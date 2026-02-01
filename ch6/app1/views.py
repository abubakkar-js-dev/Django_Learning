from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def  home(request):
    return HttpResponse('This is Home Page');

def myapp(request):
    return HttpResponse("Hello this is my first application on Django");

def learn_django(req):
    return HttpResponse('Hello django')

def learn_python(req):
    return HttpResponse('<h2>Hello Python</h2>')

def learn_math(req):
    result = 2 + 2
    text = '2 + 2'
    o = f"<h3>{text} = {result}</h3>"
    return HttpResponse(o)

def learn_php(req):
    person = {"name": 'A'}
    lang = '<h2>hello PHP</h2>'
    return HttpResponse(lang)