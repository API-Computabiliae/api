import os

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

from .models import Pdf, Users, File, Chat
from .serializers import UserSerializer, FileSerializer, ChatSerializer
from .controller import chunk_pdf, find_matches, answer_question


class PdfView(APIView):
    def get(self, request):
        pdf = Pdf.objects.filter().all()

        data = []
        for pdf in pdf:
            data.append({
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

        chunks = Pdf.objects.filter(name=name).first()

        if chunks is None or not os.path.exists("files/" + file.name):
            file = File.objects.create(name=name, size=size, file=file)
            file.save()

            chunks = chunk_pdf("files/" + file.name)

            if chunks == []:
                os.remove("files/" + file.name)
                return Response(data={'message': 'File not found'}, status=status.HTTP_404_NOT_FOUND)
            data = ({
                'name': name,
                'size': size,
                'content': chunks[0],
            })

            data_pdf = Pdf.objects.create(name=file.name, content=chunks[0])
            data_pdf.save()      

        else:
            data = ({
                'name': name,
                'size': size,
                'content': chunks.content,
            })

        return Response(data=data, status=status.HTTP_201_CREATED)


class ChatView(APIView):
    serializer_class = ChatSerializer
    def post (self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        question = serializer.validated_data.get('message')
        name = serializer.validated_data.get('name')

        file = File.objects.filter(name=name).first()

        chunks = Pdf.objects.filter(name=name).first()

        matches = find_matches(chunks.content, question)

        for chunk_id in matches.keys():
            chunk = chunks.content[chunk_id]
            breakpoint()
            data = answer_question(chunk, question)
            break

        chat = Chat.objects.create(file=file, question=question, answer=data)
        chat.save()
        
        return Response(data=data, status=status.HTTP_200_OK)
