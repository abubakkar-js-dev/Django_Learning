
from django.contrib import admin
from django.urls import path
from app1.views import home,learn_python

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('py/',learn_python,{'status': 'ok'}),
    path('dj/',learn_python),
]
