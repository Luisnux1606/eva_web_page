from django.db import models
from ckeditor.fields import RichTextField 
# Create your models here.
class AboutMe(models.Model):

    title = models.CharField(verbose_name="Titulo",max_length=200)
    content = RichTextField(verbose_name="Contenido")
    image = models.ImageField(verbose_name="imagen", upload_to="about",blank=True)
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edicion")

    class Meta:
        verbose_name = "AboutMe"
        verbose_name_plural = "AboutMe"
        ordering = ['title']

    def __str__(self):
        return self.title

