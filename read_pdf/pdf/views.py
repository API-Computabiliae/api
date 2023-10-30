from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

from .models import Pdf


class PdfView(APIView):  
    def get(self, request):

        pdf_data = Pdf.objects.all()

        data = []
        for pdf in pdf_data:
            data.append({
                'id': pdf.id,
                'name': pdf.name,
                'content': pdf.content,
            })
        
        return Response(data=data, status=status.HTTP_200_OK)