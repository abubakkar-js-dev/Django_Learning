from django.urls import path
from student.views import students,registation

urlpatterns = [
    path('',students,name='students'),
    path('register/',registation, name='registation')
]
