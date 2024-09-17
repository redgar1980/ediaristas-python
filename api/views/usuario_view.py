from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers import usuario_serializer, editar_usuario_serializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status as status_http

class Usuario(APIView):
    def post(self, request, format=None):
        serializer_usuario = usuario_serializer.UsuarioSerializer(data=request.data,
                                                        context={"request": request})
        if serializer_usuario.is_valid():
            usuario_criado = serializer_usuario.save()
            serializer_usuario = usuario_serializer.UsuarioSerializer(usuario_criado)
            return Response(serializer_usuario.data, status=status_http.HTTP_201_CREATED)
        return Response(serializer_usuario.errors, status=status_http.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        usuario_antigo = Usuario.objects.get(id=request.user.id)
        serializer_usuario = editar_usuario_serializer.EditarUsuarioSerializer(
            usuario_serializer, data=request.data, context={"request": request})
        if serializer_usuario.is_valid():
            serializer_usuario.save()
            return Response(serializer_usuario.data, status=status_http.HTTP_200_OK)
        return Response(serializer_usuario.errors, status=status_http.HTTP_400_BAD_REQUEST)