from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

from .models import Pdf, Users
from .serializers import UserSerializer

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
    

class UserView(APIView):
    serializer_class = UserSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')

        breakpoint()
        user = Users.objects.filter(email=email, password=password)
        if user.count() == 0:
            return Response(data={'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(data={'message': 'User found'}, status=status.HTTP_200_OK)
