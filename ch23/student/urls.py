from django.urls import path
from student.views import all_students,studentDetails

urlpatterns = [
    path('',all_students,name='all_students'),
    path('<int:id>/',studentDetails,name='student_details'),
]
