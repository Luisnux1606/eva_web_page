from django.contrib import admin
from .models import Footer

# Register your models here.

class FooterAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Footer,FooterAdmin)    
