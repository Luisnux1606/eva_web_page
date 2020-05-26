from .models import Footer 

def ctx_dict(request):
    ctx = {} #ctx = {'text':'hola'}
    footer = Footer.objects.all()
    ctx = {'footer':footer}
    return ctx
