from django.shortcuts import render


# Create your views here.

def home(req):
    return render(req,'courses/courses.html')

def blogs(req):

    descriptions = "This is a high parformance blogs for python developer. Everybody should read and follow the steps. As a result they can learn a lot";
    overview = {"category": 'Technology','total_blogs':3,'descriptions':descriptions}

    return render(req,'courses/blogs.html',context=overview) # just variable name or a dictionany could be as a context instat of using context =