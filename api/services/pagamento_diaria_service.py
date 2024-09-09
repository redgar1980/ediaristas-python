import pagarme
import environ
from rest_framework import serializers
from ..models import Pagamento
from .diaria_service import atualizar_status_diaria, listar_diaria_id

env = environ.Env()

env.read_env(env.str('ENV_PATH','./ediaristas/.env'))

pagarme.authentication_key(env('PAGARME_KEY'))

def realizar_pagamento(diaria, card_hash):
    diaria = listar_diaria_id(diaria.id)
    diaria = listar_diaria_id(diaria.id)
    cliente = diaria.cliente
    params = {
        "amount": float(diaria.preco) * 100,
        "card_hash": card_hash,
        "custormer": {
            "external_id": cliente.id,
            "name": cliente.nome_completo,
            "type": "individual",
            "country": "br",
            "email": cliente.email,
            "documents": [
                {
                    "type": "cpf",
                    "number": cliente.cpf
                }
            ]
        },
        "items": [
            {
                "id": diaria.id,
                "title": "Diária e-diaristas",
                "unit_price": float(diaria.preco) * 100,
                "quantity": "1",
                "tangible": False
            }
        ]
    }
    transacao = pagarme.transaction.create(params)
    print(transacao['status'])
    if transacao['status'] == 'paid':
        Pagamento.objects.create(status="pago",
            valor=diaria.preco, transacao_id=transacao['tid'],
            diaria=diaria)
        atualizar_status_diaria(diaria.id, 2)
        return
    else:
        Pagamento.objects.create(status="reprovado",
            valor=diaria.preco, transacao_id=transacao['tid'],
            diaria=diaria)
        atualizar_status_diaria(diaria.id, 1)
        raise serializers.ValidationError("Pagamento recusado")
    
def realizar_pagamento_test(diaria, card_hash):
    Pagamento.objects.create(status="pago",
        valor=diaria.preco, transacao_id="12a9aqwe",
        diaria=diaria)
    atualizar_status_diaria(diaria.id, 2)
    return

def cancelar_pagamento(diaria_id, penalidade):
    diaria = listar_diaria_id(diaria_id)
    pagamento = Pagamento.objects.filter(diaria=diaria_id).get(status='pago')
    valor = (pagamento.valor / 2) if penalidade else pagamento.valor
    cancelamento = pagarme.transaction.refund(pagamento.transacao_id, {"amount": valor})
    if cancelamento['refunded_amount'] != valor:
        raise serializers.ValidationError("Erro ao estornar o pagamento")
    return Pagamento.objects.create(status='cancelado', valor=valor,
                                    transacao_id=pagamento.transacao_id, 
                                    diaria=diaria)