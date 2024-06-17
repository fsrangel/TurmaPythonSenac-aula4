def validar_titulo(titulo):
    if not titulo:
        raise ValueError("O título não pode ser vazio.")
    if len(titulo) > 100:
        raise ValueError("O título não pode ter mais de 100 caracteres.")

def validar_descricao(descricao):
    if not descricao:
        raise ValueError("A descrição não pode ser vazia.")
    if len(descricao) > 500:
        raise ValueError("A descrição não pode ter mais de 500 caracteres.")
