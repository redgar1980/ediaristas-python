from rest_framework.views import APIView
from ..services import diaria_service
from ..serializers import pagamento_diaria_serializer

class PagamentoDiaria(APIView):
    def post(self, request, diaria_id, formart=None):
        diaria = diaria_service.listar_diaria_id(diaria_id)
        serializer_pagamento = pagamento_diaria_serializer.PagamentoDiariaSerializer(
            data=request.data)
        if serializer_pagamento.is_valid():
            card_hash = serializer_pagamento.validated_data["card_hash"]
            if diaria.status == 1:
                # realizar pagamento
                pass
