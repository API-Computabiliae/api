from rest_framework import serializers


class PdfSerializer(serializers.Serializer):
    name = serializers.CharField()
    content = serializers.CharField()


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class FileSerializer(serializers.Serializer):
    name = serializers.CharField()
    size = serializers.IntegerField()
    file = serializers.FileField()


class ChatSerializer(serializers.Serializer):
    message = serializers.CharField()
    name = serializers.CharField()
