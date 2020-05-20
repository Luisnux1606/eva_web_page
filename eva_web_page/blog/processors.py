from .models import Category 
from slide.models import Slide

def ctx_dict(request):
    ctx = {} #ctx = {'text':'hola'}
    category = Category.objects.all()
    slide = Slide.objects.all()
    ctx = {'categories':category,'slides':slide}
    return ctx


