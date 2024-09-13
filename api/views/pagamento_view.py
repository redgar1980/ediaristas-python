from rest_framework import APIView
from rest_framework.response import Response
from rest_framework import status as status_http
from ..models import Diaria, Pagamento

class Pagamento(APIView):
    def get(self, request, format=None):
        # pegar a lista de pagamentos do usuário logado
        diarias_pagamento = Diaria.objects.filter(diarista=request.user.id).filter(status__in=[4, 6, 7])
        pagamentos = Pagamento.objects.filter(diaria__in=diarias_pagamento)
        # serializar os dados
        # retornar os pagamentos do usuário