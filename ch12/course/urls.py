from django.urls import path
from course.views import learn_django

urlpatterns = [
    path('django',learn_django,name="learn_django")
]
