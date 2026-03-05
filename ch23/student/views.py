from django.shortcuts import render
from student.models import Profile

# Create your views here.

def all_students(req):
    students = Profile.objects.all()
    return render(req,'student/allStudents.html',{'students': students})
