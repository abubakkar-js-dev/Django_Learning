from django.contrib import admin
from django.urls import path
from blogs.views import blogs,single_blog

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',blogs,name='blogs'),
    path('blog/',single_blog,name='single_blog')
]