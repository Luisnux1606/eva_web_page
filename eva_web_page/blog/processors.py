from .models import Category 
from slide.models import Slide
from about.models import AboutMe
from django.shortcuts import get_object_or_404

def ctx_dict(request):
    ctx = {} #ctx = {'text':'hola'}
    category = Category.objects.all()
    slide = Slide.objects.all()
    about_me = get_object_or_404(AboutMe, id=2)
    ctx = {'categories':category,'slides':slide,'about_me':about_me}
    return ctx
