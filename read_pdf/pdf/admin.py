from django.contrib import admin
from .models import Pdf, Users

# Register your models here.

class PdfAdmin(admin.ModelAdmin):
    list_display = ('name', 'content')
    search_fields = ('name', 'content')


class UsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')

admin.site.register(Pdf, PdfAdmin)
admin.site.register(Users, UsersAdmin)