from django.contrib import admin
from .models import Slide

# Register your models here.
class SlideAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Slide,SlideAdmin)    
