from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import AboutMe
# Create your views here.
def about(request):
    aboutMe = get_object_or_404(AboutMe,id=1)
    return render(request,"about/about.html",{'about_me':aboutMe}) 

