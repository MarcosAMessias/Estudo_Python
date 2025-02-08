# Função principal que controla o programa
def main():
    # Cria uma lista vazia para armazenar as tarefas
    tarefas = []

    # Loop infinito para exibir o menu até que o usuário escolha sair
    while True:
        # Exibe as opções do menu
        print("\n1. Adicionar Tarefa\n2. Exibir Tarefas\n3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha =="1":
            # Adicionar uma nova tarefa à lista
            tarefa = input("Digite a tarefa: ")
            tarefas.append(tarefa)
        elif escolha == "2":
            # Exibe todas as tarefas na lista
            if tarefas:
                # Se houver tarefas, exibe cada uma com seu índice
                for idx, tarefa in enumerate(tarefas, 1):
                    print(f"{idx}. {tarefa}")
            else:
                    # Se não houver tarefas, informa o usuário
                    print("Nenhuma tarefa adicionada.")
        elif escolha == "3":
            # Sai do loop e encerra o programa 
            break
        else:
            # Informa ao usuário que a opção escolhida é inválida 
            print("Opção inválida, tente novamente.")

# Verifica se o script está sendo executado diretamente 
if __name__ == "__main__":
    main()