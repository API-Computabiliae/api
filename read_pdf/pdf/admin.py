from django.contrib import admin
from .models import Pdf

# Register your models here.

class PdfAdmin(admin.ModelAdmin):
    list_display = ('name', 'content')
    search_fields = ('name', 'content')

admin.site.register(Pdf, PdfAdmin)