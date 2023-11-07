from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path
from pdf.views import PdfView, UserView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pdf', PdfView.as_view(), name='pdf'),
    path('login', UserView.as_view(), name='login')
]