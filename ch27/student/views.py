from django.shortcuts import render
from student.forms import Registation,Login

# Create your views here.

def students(req):
    return render(req,'student/students.html')

def registation(req):
    formData = Registation(field_order=['email','city'])
    return render(req,'student/registation.html',{'form': formData})

def login(req):
    # formData = Login(auto_id='login_%s')
    formData = Login(auto_id=True,initial={'email': 'username@example.com', 'password': 1234})
    return render(req,'student/login.html',{'form': formData})
