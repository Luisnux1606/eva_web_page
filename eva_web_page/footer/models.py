from django.db import models

# Create your models here.

class Footer(models.Model):
    image = models.ImageField(verbose_name="imagen", upload_to="footer")

    created = models.DateTimeField(auto_now_add=True,verbose_name="fecha creacion")    #auto now django not show in admin
    updated = models.DateTimeField(auto_now=True,verbose_name="fecha modificacion")

    class Meta:
        verbose_name = "foto_pie"
        verbose_name_plural = "fotos_pie"
        ordering = ["-created"]

    def __str__(self):
        return str(self.id)
