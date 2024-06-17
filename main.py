from gerenciador_tarefas import GerenciadorTarefas
from validador_tarefa import validar_titulo, validar_descricao
from menu import exibir_menu

def main():
    gerenciador = GerenciadorTarefas()
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            titulo = input("Título da Tarefa: ")
            descricao = input("Descrição da Tarefa: ")
            try:
                validar_titulo(titulo)
                validar_descricao(descricao)
                gerenciador.adicionar_tarefa(titulo, descricao)
                print("Tarefa adicionada com sucesso!")
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == '2':
            tarefas = gerenciador.visualizar_tarefas()
            if tarefas:
                for tarefa in tarefas:
                    print(tarefa)
            else:
                print("Nenhuma tarefa cadastrada.")

        elif opcao == '3':
            titulo = input("Título da Tarefa: ")
            tarefa = gerenciador.localizar_tarefa(titulo)
            if tarefa:
                print(tarefa)
            else:
                print("Tarefa não encontrada.")

        elif opcao == '4':
            titulo = input("Título da Tarefa: ")
            novo_status = input("Novo Status (pendente/concluída): ")
            if novo_status not in ['pendente', 'concluída']:
                print("Status inválido. Use 'pendente' ou 'concluída'.")
                continue
            tarefa = gerenciador.atualizar_status_tarefa(titulo, novo_status)
            if tarefa:
                print("Status da tarefa atualizado com sucesso!")
            else:
                print("Tarefa não encontrada.")

        elif opcao == '5':
            titulo = input("Título da Tarefa: ")
            tarefa = gerenciador.remover_tarefa(titulo)
            if tarefa:
                print("Tarefa removida com sucesso!")
            else:
                print("Tarefa não encontrada.")

        elif opcao == '6':
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
