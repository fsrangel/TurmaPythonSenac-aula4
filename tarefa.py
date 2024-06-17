class Tarefa:
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
        self.status = 'pendente'

    def __str__(self):
        return f'Título: {self.titulo}, Descrição: {self.descricao}, Status: {self.status}'
