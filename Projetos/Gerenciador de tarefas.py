import os # Importa o módulo para manipular arquivos

# Lista que armazenará as tarefas. Cada tarefa é um dicionário com 'nome' e 'status'

tarefas= []  # criando uma lista

# Função para adicionar uma nova tarefa
def adicionar_tarefa():
    nome_tarefa = input("Digite o nome da tarefa: ").strip()
    if nome_tarefa:
        tarefas.append({'nome': nome_tarefa, 'concluida': False})
        print(f"Tarefa '{nome_tarefa}' adicionada com sucesso!")
    else:
        print("O nome da tarefa não pode estar vazio.")

# Função para exibir todas as tarefas
def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return 
    
    print("\n ******** Lista de Tarefas *******")
    for i, tarefa in enumerate(tarefas, start=1):
        status = "Concluída" if tarefa ['concluida'] else "Pendente"
        print(f"{i}. {tarefa['nome']} - {status}")

# Função para marcar uma tarefa como concluída
def concluir_tarefa():
    listar_tarefas() # A definição de 'concluir_tarefa' chama 'listar_tarefas'
    try:
        indice = int(input("\nDigite o número da tarefa que desja marcar como concluída :"))
        if 1 <= indice <= len(tarefas):
            tarefas[indice - 1]['concluida'] = True
            print(f"Tarefa '{tarefas[indice - 1]['nome']}'marcada como concluída!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")

# Função para remover uma tarefa
def remover_tarefa():
    listar_tarefas()
    try:
        indice = int(input("\nDigite o número da tarefa que deseja remover: "))
        if 1 <= indice <= len(tarefas):
            tarefa_removida = tarefas.pop(indice -1) # POP retira a tarefa
            print(f"Tarefa '{tarefa_removida['nome']}' removida com sucesso!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")

#  Função para salvar as tarefas em um arquivo
def salvar_tarefas():
    with open("tarefas.txt", "w") as arquivo:
        for tarefa in tarefas:
            # Salva o nome e o status da tarefa separados por "|"
            linha = f"{tarefa['nome']}|{'Concluída' if tarefa['concluida'] else 'Pendente'}\n"  
            arquivo.write(linha)
    print("Tarefas salvas no arquivo 'tarefas.txt'.")      

# Função para carregar tarefas de um arquivo
def carregar_tarefas():
    if not os.path.exists("tarefas.txt"):
        return
    
    with open("tarefas.txt", "r") as arquivo:
        for linha in arquivo:
            nome, status = linha.strip().split("|")
            tarefas.append({'nome':nome, 'concluida':status == "Concluída"})
    print("Tarefas carregadas do arquivo 'tarefas.txt'.")

# Função principal que exibe o menu e gerencia as opções do usuário
def menu():
    carregar_tarefas() # Carrega tarefas ao iniciar o programa

    while True:
        print("\n**** Gerenciador de Lista de Tarefas ****")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Remover tarefa")
        print("5. Salvar tarefas")
        print("6. Sair")

        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                adicionar_tarefa()
            elif opcao == 2:
                listar_tarefas()
            elif opcao == 3:
                concluir_tarefa()
            elif opcao == 4:
                remover_tarefa()
            elif opcao == 5:
                salvar_tarefas()
            elif opcao == 6:
                print("Saindo... Até mais! \U0001F44B")
                salvar_tarefas() # Salva automaticamente ao sair
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Por favor, digite um número válido. (1-6)")

# Ponto de entrada do programa
if __name__ == "__main__":
    menu()
