import sqlite3  # Biblioteca para interagir com o banco de dados SQLite

def conectar_banco():
    """Conecta ao banco de dados SQLite e cria o arquivo 'sistema.db' se ele não existir."""
    conexao = sqlite3.connect("sistema.db")
    return conexao

def criar_tabelas(conexao):
    """Cria as tabelas 'clientes', 'produtos' e 'pedidos' no banco de dados, caso ainda não existam."""
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        contato TEXT
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        quantidade INTEGER NOT NULL                
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pedidos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER NOT NULL,
        produto_id INTEGER NOT NULL,
        quantidade INTEGER NOT NULL,
        FOREIGN KEY (cliente_id) REFERENCES clientes (id),
        FOREIGN KEY (produto_id) REFERENCES produtos (id)
    )
    """)
    conexao.commit()
    print("Tabelas criadas ou já existem no banco de dados.")

def inserir_cliente(conexao):
    """Insere um novo cliente na tabela 'clientes'."""
    nome = input("Nome do cliente: ").strip()
    contato = input("Contato do cliente: ").strip()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO clientes (nome, contato) VALUES (?, ?)", (nome, contato))
    conexao.commit()
    print("Cliente inserido com sucesso!")

def inserir_produto(conexao):
    """Insere um novo produto na tabela 'produtos'."""
    nome = input("Nome do produto: ").strip()
    preco = float(input("Preço do produto: "))
    quantidade = int(input("Quantidade em estoque: "))
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO produtos (nome, preco, quantidade) VALUES (?, ?, ?)", (nome, preco, quantidade))
    conexao.commit()
    print("Produto inserido com sucesso!")

def inserir_pedido(conexao):
    """Insere um novo pedido na tabela 'pedidos'."""
    cliente_id = int(input("ID do cliente: "))
    produto_id = int(input("ID do produto: "))
    quantidade = int(input("Quantidade do produto: "))
    cursor = conexao.cursor()
    cursor.execute("""
    INSERT INTO pedidos (cliente_id, produto_id, quantidade)
    VALUES (?, ?, ?)
    """, (cliente_id, produto_id, quantidade))
    conexao.commit()
    print("Pedido inserido com sucesso!")

def visualizar_tabelas(conexao):
    """Exibe os dados das tabelas 'clientes', 'produtos' e 'pedidos'."""
    cursor = conexao.cursor()
    print("\nClientes:")
    for cliente in cursor.execute("SELECT * FROM clientes"):
        print(cliente)

    print("\nProdutos:")
    for produto in cursor.execute("SELECT * FROM produtos"):
        print(produto)

    print("\nPedidos:")
    for pedido in cursor.execute("SELECT * FROM pedidos"):
        print(pedido)

def main():
    """Função principal que gerencia o fluxo do sistema."""
    print("Bem-vindo ao Sistema de Gerenciamento de Estoque!")
    conexao = conectar_banco()
    criar_tabelas(conexao)

    while True:
        print("\nMenu do Sistema:")
        print("1. Inserir cliente")
        print("2. Inserir produto")
        print("3. Inserir pedido")
        print("4. Visualizar tabelas")
        print("5. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            inserir_cliente(conexao)
        elif opcao == "2":
            inserir_produto(conexao)
        elif opcao == "3":
            inserir_pedido(conexao)
        elif opcao == "4":
            visualizar_tabelas(conexao)
        elif opcao == "5":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

    conexao.close()

if __name__ == "__main__":
    main()
