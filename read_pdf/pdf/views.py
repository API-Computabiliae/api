from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.

from django.http import HttpResponse
from .models import Pdf


class PdfView(APIView):
    def get(self, request):
        pdf = Pdf.objects.all()
        return render(request, 'pdf.html', {'pdf': pdf})