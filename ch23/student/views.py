from django.shortcuts import render, get_object_or_404
from student.models import Profile

# Create your views here.

def all_students(req):
    students = Profile.objects.all()
    return render(req,'student/allStudents.html',{'students': students})


def studentDetails(req,id):
    # student=Profile.objects.get(id=id)
    student=get_object_or_404(Profile,id=id)
     
    
    return render(req,'student/studentDetails.html',{'student': student})