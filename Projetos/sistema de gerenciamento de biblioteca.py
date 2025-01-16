"""
Sistema de gerenciamento de biblioteca em python
Dicionário para armazenar informações sobre os livros
Estrutura:{"nome_do_livro":{"disponivel":bool, "emprestado_para":str ou None}}
"""
biblioteca = {}

def adicionar_livro():
    """
    Adiciona um novo livro à biblioteca.
    """
    nome_livro = input("Digite o nome do livro a ser adicionado: ").strip()
    if nome_livro in biblioteca:
        print(f"O livro '{nome_livro}' já está na biblioteca.")
    else:
        biblioteca[nome_livro] = {"disponivel":True ,"emprestado_para": None}
        print(f"O livro '{nome_livro}' foi adicionado com sucesso!")

def emprestar_livro():
    """
    Permite o empréstimo de um livro disponível.
    """
    nome_livro = input("Digite o nome do livro que deseja emprestar: ").strip()
    if nome_livro in biblioteca:
        if biblioteca[nome_livro]["disponivel"]:
            nome_usuario = input("Digite o nome do usuário que está emprestando o livro: ").strip()
            biblioteca[nome_livro]["disponivel"] = False
            biblioteca[nome_livro]["emprestado_para"] = nome_usuario
            print(f"O livro '{nome_livro}' foi emprestado para {nome_usuario}.")
        else:
            print(f"O livro '{nome_livro} já está emprestado para {biblioteca[nome_livro]['emprestado_para']}")
    else:
        print(f"O livro '{nome_livro}' não existe na biblioteca.")
def devolver_livro():
    """
    Permite a devolução de um livro emprestado.
    """
    nome_livro = input("Digite o nome do livro que deseja devolver: ").strip()
    if nome_livro in biblioteca:
        if not biblioteca[nome_livro]["disponivel"]:
            biblioteca[nome_livro]["disponivel"] = True
            usuario = biblioteca[nome_livro]["emprestado_para"]
            biblioteca[nome_livro]["emprestado_para"] = None
            print(f"O livro '{nome_livro}' foi devolvido por {usuario}.")
        else:
            print(f"O livro '{nome_livro}' já está disponível na biblioteca.")
    else:
        print(f"O livro '{nome_livro}' não existe na biblioteca.")

def consultar_livros():
    """
    Exibe todos os livros na biblioteca com seu status.
    """
    if biblioteca:
        print("\nLista de livros na biblioteca:")
        for livro, dados in biblioteca.items():
            status = "Disponível" if dados ["disponivel"] else f"Emprestado para {dados['emprestado_para']}"
            print(f"- {livro}:{status}")
    else:
        print("A biblioteca está vazia.")

def exibir_menu():
    # Exibe o menu principal com as opções do sistema.
    print("\n ***** \U0001F4DA Sistema de Gerenciamento de Livros \U0001F4DA *****")
    print("1. Adicionar Livro")
    print("2. Emprestar Livro")
    print("3. Devolver Livro")
    print("4. Consultar Livro")
    print("5. Sair")

def sistema_de_biblioteca():
    # Função principal que controla o fluxo do sistema de biblioteca.
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            adicionar_livro()
        elif opcao == "2":
            emprestar_livro()
        elif opcao == "3":
            devolver_livro()
        elif opcao == "4":
            consultar_livros()
        elif opcao == "5":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Inicia o sistema de biblioteca
if __name__ == "__main__":
    sistema_de_biblioteca()


