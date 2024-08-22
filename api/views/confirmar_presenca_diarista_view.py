from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as status_http
from ..permissions import cliente_permission
from ..services import diaria_service

class ConfirmarPresencaDiaristaID(APIView):
    permission_classes = [cliente_permission]

    def patch(self, request, diaria_id, format=None):
        diaria = diaria_service.listar_diaria_id(diaria_id)
        self.check_object_permissions(self.request, diaria)
        # implementar no service a lógica para confirmar a presenca
        return Response("Presença confirmada com sucesso", status=status_http.HTTP_200_OK)