from django.contrib import admin
from django.views.generic import TemplateView
from pdf.views import PdfView
from django.urls import re_path
from django.urls import path


app_name = 'pdf'


urlpatterns = [
    path('path', PdfView.as_view(), name='pdf'),
]