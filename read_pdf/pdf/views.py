import os

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

from .models import Pdf, Users, File
from .serializers import UserSerializer, FileSerializer
from .controller import chunk_pdf, find_matches


class PdfView(APIView):
    def get(self, request):
        pdf = Pdf.objects.filter().first()

        data = []
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

        user = Users.objects.filter(email=email, password=password)
        if user.count() == 0:
            return Response(data={'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(data={'message': 'User found'}, status=status.HTTP_200_OK)
    

class FileView(APIView):
    serializer_class = FileSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        name = serializer.validated_data.get('name')
        size = serializer.validated_data.get('size')
        file = serializer.validated_data.get('file')

        if not os.path.exists('files/'):
            os.makedirs('files/')
            file = File.objects.create(name=name, size=size, file=file)
            file.save()

            chunks = chunk_pdf("files/" + file.name)

            data = ({
                'name': name,
                'size': size,
                'content': chunks[0],
            })

            data_pdf = Pdf.objects.create(name=file.name, content=chunks[0])
            data_pdf.save()      
        
            # matches = find_matches(chunks, keywords)
        else:
            chunks = Pdf.objects.filter(name=name).first()

            data = ({
                'name': name,
                'size': size,
                'content': chunks.content,
            })
        return Response(data=data, status=status.HTTP_201_CREATED)
