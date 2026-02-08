from django.urls import path
from course.views import courses

urlpatterns = [
    path('',courses,name='course'),

]
