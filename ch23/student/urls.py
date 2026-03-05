from django.urls import path
from student.views import all_students

urlpatterns = [
    path('',all_students,name='all_students')
]
