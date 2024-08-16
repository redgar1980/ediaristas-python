from .diaria_service import listar_diaria_id

def selecionar_diarista_diaria(diaria_id):
    diaria = listar_diaria_id(diaria_id)
    candidatas = diaria.candidatas.all()
    diarista_compativel = []
    for candidata in candidatas:
        # calcular o indice de compatibilidade
        pass