from rest_framework import serializers
from ..models import AvaliacaoDiaria

def verificar_avaliacao_usuario(diaria_id, usuario_id):
    avaliacao_diaria = AvaliacaoDiaria.objects.filter(diaria=diaria_id)
    for avaliacao in avaliacao_diaria:
        if avaliacao.avaliador.id == usuario_id:
            return True
    return False

def verificar_avaliacao(diaria_id):
    avaliacoes_diaria = AvaliacaoDiaria.objects.filter(diaria=diaria_id)
    return avaliacoes_diaria.count()