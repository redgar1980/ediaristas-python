from rest_framework.response import Response
from rest_framework import serializers, status as status_http
from rest_framework.views import APIView
from ..serializers import avaliacao_diaria_serializer
from ..permissions import dono_permission
from ..models import AvaliacaoDiaria
from ..services import diaria_service, usuario_service, avaliacao_diaria_service

class AvaliacaoDiariaID(APIView):
    permission_classes = [dono_permission.DonoPermission,]

    def patch(self, request, diaria_id, format=None):
        diaria = diaria_service.listar_diaria_id(diaria_id)
        if diaria.status != 4:
            raise serializers.ValidationError(
                "Apenas diárias com status 4 podem ser avaliadas")
        usuario_logado = usuario_service.listar_usuario_id(request.user.id)
        self.check_object_permissions(self.request, diaria)
        serializer_avaliacao_diaria = avaliacao_diaria_serializer.AvaliacaoDiariaSerializer(
            data=request.data)
        # verificar se o usuário que está avaliando não tinha avaliado anteriormente
        if avaliacao_diaria_service.verificar_avaliacao_usuario(diaria_id, usuario_logado.id):
            raise serializers.ValidationError("Esse usuário já avaliou a diária")
        if serializer_avaliacao_diaria.is_valid():
            if usuario_logado.tipo_usuario == 1:
                avaliado = diaria.diarista
            else:
                avaliado = diaria.cliente
            serializer_avaliacao_diaria.save(visibilidade=1, diaria=diaria, 
                avaliador=usuario_logado, avaliado=avaliado)
            # atualizar a nota do usuário que está sendo avaliado
            media_usuario = AvaliacaoDiaria.avaliacao_objects.reputacao_usuario(avaliado.id)
            usuario_service.atualizar_reputacao_usuario(avaliado, media_usuario['nota__avg'])
            # verificar se os dois usuários avaliaram
            if avaliacao_diaria_service.verificar_avaliacao(diaria_id) == 2:
                # alterar o status da diária para 6
                diaria_service.atualizar_status_diaria(diaria_id, 6)
            # retornar os dados da avaliação
            return Response(serializer_avaliacao_diaria.data, status=status_http.HTTP_201_CREATED)
        return Response(serializer_avaliacao_diaria.errors, status=status_http.HTTP_400_BAD_REQUEST)