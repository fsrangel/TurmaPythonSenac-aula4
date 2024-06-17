from tarefa import Tarefa

class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, titulo, descricao):
        tarefa = Tarefa(titulo, descricao)
        self.tarefas.append(tarefa)

    def visualizar_tarefas(self):
        return self.tarefas

    def localizar_tarefa(self, titulo):
        for tarefa in self.tarefas:
            if tarefa.titulo == titulo:
                return tarefa
        return None

    def atualizar_status_tarefa(self, titulo, novo_status):
        tarefa = self.localizar_tarefa(titulo)
        if tarefa:
            tarefa.status = novo_status
            return tarefa
        return None

    def remover_tarefa(self, titulo):
        tarefa = self.localizar_tarefa(titulo)
        if tarefa:
            self.tarefas.remove(tarefa)
            return tarefa
        return None
