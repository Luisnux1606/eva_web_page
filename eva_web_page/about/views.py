from django.shortcuts import render
from .models import AboutMe
# Create your views here.
def about(request):
    aboutMe = AboutMe.objects.get(pk=1)
    return render(request,"about/about.html",{'about_me':aboutMe}) 

