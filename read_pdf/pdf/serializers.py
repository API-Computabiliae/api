from rest_framework import serializers


class PdfSerializer(serializers.Serializer):
    name = serializers.CharField()
    content = serializers.CharField()


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
