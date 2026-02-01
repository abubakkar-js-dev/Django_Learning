from django.urls import path
from courses.views import home,blogs

urlpatterns = [
    path('',home,name='home'),
    path('blogs/',blogs,name='blogs')
]
