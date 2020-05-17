from .models import Category 

def ctx_dict(request):
    ctx = {} #ctx = {'text':'hola'}
    category = Category.objects.all()
    ctx = {'categories':category}
    return ctx


