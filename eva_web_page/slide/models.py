from django.db import models

# Create your models here.

class Slide(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    subtitle = models.CharField(max_length=200, verbose_name="Subtitulo")
    fecha= models.DateTimeField(auto_now_add=True,verbose_name="fecha")
    image = models.ImageField(verbose_name="imagen", upload_to="services")

    created = models.DateTimeField(auto_now_add=True,verbose_name="fecha creacion")    #auto now django not show in admin
    updated = models.DateTimeField(auto_now=True,verbose_name="fecha modificacion")

    class Meta:
        verbose_name = "slide"
        verbose_name_plural = "slides"
        ordering = ["-created"]

    def __str__(self):
        return self.title
