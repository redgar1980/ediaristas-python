from rest_framework import serializers

class FotoUsuarioSerializer(serializers.Serializer):
    foto_usuario = serializers.ImageField()