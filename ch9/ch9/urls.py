
from django.contrib import admin
from django.urls import path,include
from courses.views import courses,learn_python,learn_javascript



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('blogs/',include('blogs.urls')),
    path('courses/',include([
        path('',courses,name='courses'),
        path('py/',learn_python,name='learn_python'),
        path('js/',learn_javascript,name='learn_javascript')
    ]))
]
