from django.shortcuts import render
from student.forms import Registation

# Create your views here.

def students(req):
    return render(req,'student/students.html')

def registation(req):
    formData = Registation()
    return render(req,'student/registation.html',{'form': formData})
