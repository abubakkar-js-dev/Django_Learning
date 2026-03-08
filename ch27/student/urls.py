from django.urls import path
from student.views import students,registation,login

urlpatterns = [
    path('',students,name='students'),
    path('register/',registation, name='registation'),
    path('login/',login, name='login')
]
