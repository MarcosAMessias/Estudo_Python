"""
Fluxo de Navegação
O usuário acessa a página de listagem e visualiza os produtos ordenados.
Ao clicar em "Cadastrar Novo Produto", é redirecionado para o formulário.
Preenche os campos e clica em "Salvar".
Após o cadastro, é redirecionado automaticamente para a listagem.
Autor: Marcos A. Messias data:16/01/2025
"""


# Lista para armazenar os produtos cadastrados
produtos = []

def cadastrar_produto():
    #Função para cadastrar um novo produto
    nome = input("\nNome do produto: ")  # Solicita o nome do produto
    descricao = input("Descrição do produto: ")  # Solicita a descrição do produto
    valor = float(input("Valor do produto (ex: 29.99 \U0001F4B5): "))  # Solicita o valor e converte para float
    # Verifica se o produto está disponível para venda (Sim -> True, Não -> False)
    disponivel = input("Disponível para venda (Sim/Não): ").strip().lower() == "sim"  
    # Adiciona o produto na lista como um dicionário
    produtos.append({"nome": nome, "descricao": descricao, "valor": valor, "disponivel": disponivel})
    print("Produto cadastrado com sucesso!\n")  # Confirma o cadastro do produto
    listar_produtos()  # Após cadastrar, redireciona para a listagem

def listar_produtos():
    #Função para listar os produtos cadastrados.
    if not produtos:  # Verifica se não há produtos cadastrados
        print("\nNenhum produto cadastrado.\n")  # Exibe mensagem caso a lista esteja vazia
    else:
        print("\n--- Produtos ---")  # Cabeçalho da listagem
        # Ordena os produtos por valor (do menor para o maior) e exibe cada um
        for p in sorted(produtos, key=lambda x: x["valor"]):  
            print(f"{p['nome']:<20} R$ {p['valor']:.2f}")  # Exibe nome e valor formatados
    # Oferece ao usuário as opções de cadastrar um novo produto ou sair
    if input("\n1. Novo produto | 2. Sair: ").strip() == "1":
        cadastrar_produto()  # Se a opção for "1", chama a função de cadastro

# Mensagem de boas-vindas ao iniciar o programa
print("Bem-vindo ao sistema de produtos\n Oak Tecnologia!\n")
print("Tenho meus projetos e outros códigos aqui  \U0001F447")
print("https://github.com/MarcosAMessias/Estudo_Python/tree/main/Projetos\n")
print("https://www.linkedin.com/in/marcos-a-messias/details/certifications/")
listar_produtos()  # Inicia exibindo a listagem

