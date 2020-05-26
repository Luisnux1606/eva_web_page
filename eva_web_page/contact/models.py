from django.db import models
from ckeditor.fields import RichTextField 

# Create your models here.
class Contact(models.Model): 
    contenido = RichTextField(verbose_name="contenido")
    created = models.DateTimeField(auto_now=True, verbose_name="creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="actualizado")

    class Meta:
        verbose_name = "contacto"
        verbose_name_plural = "contactos"
        ordering = ['-created']

    def __str__(self):
        return self.contenido

