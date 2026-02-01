from django.contrib import admin
from django.urls import path
from home.views import home,category

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',home,name='home'),
    path('category/',category,name='category')
]
