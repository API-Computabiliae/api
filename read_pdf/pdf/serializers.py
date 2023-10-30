from rest_framework import serializers


class PdfSerializer(serializers.Serializer):
    name = serializers.CharField()
    content = serializers.CharField()
