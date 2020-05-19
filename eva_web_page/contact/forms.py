from django import forms

class ContactForms(forms.Form):
    name = forms.CharField(label="Nombre", required=True,widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Escribe tu nombre aqui'} #attrs is to give a class of bootstrap  to char
    ),min_length=3 , max_length= 100)
    subject = forms.CharField(label="Asunto", required=False,widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Escribe tu asunto aqui'} #attrs is to give a class of bootstrap  to char
    ),min_length=3 , max_length= 100)

    email =forms.EmailField(label="Email",required=True, widget=forms.EmailInput(
        attrs={'class':'form-control','placeholder':'Escribe tu email aqui'}
    ),min_length=3 , max_length= 100)
    content = forms.CharField(label="Contenido",required=True, widget=forms.Textarea(
        attrs={'class':'form-control','rows':4,'cols':150,'placeholder':'Escribe tu msg aqui'}
    ),min_length=10 , max_length= 100)


