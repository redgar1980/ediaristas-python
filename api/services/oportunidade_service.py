from ..models import Usuario, Diaria

def listar_oportunidades(diarista_id):
    cidades_atendidas_usuario = Usuario.diaristas_objects.cidades_atendidas(diarista_id)
    