from django.shortcuts import render,redirect,get_object_or_404
import sys
from django.urls import reverse
from .forms import ContactForms
from .models import Contact

from django.core.mail import EmailMessage,send_mail
# Create your views here.
def contact(request):
    #print("Tipo de peticion: {}".format(request.method))
    contacto = get_object_or_404(Contact,id=1) 
    contact_form = ContactForms()  #create the form in base of form

    if request.method == "POST":    #if the request is post
        contact_form = ContactForms(data=request.POST)#fill template of form with filds
        if contact_form.is_valid():
            name = request.POST.get('name','')   #recuperate data of filds
            asunto = request.POST.get('subject','') 
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #if all is ok
            print(email)
            try: 
                 send_mail(asunto,
                         "Correo de: {} <{}>\n\nEscribio:\n\n{}".format(name,email,content),
                            email,['luisenriquegonzalezd@gmail.com'],fail_silently=False)
                 return redirect(reverse('contact')+"?ok")
            except:
                return redirect(reverse('contact')+"?fail")

    return render(request,"contact/contact.html",{'form':contact_form,'contacto':contacto})

