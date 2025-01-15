import sqlite3

# Conexão com o banco de dados SQLite
conexao = sqlite3.connect("controle_estoque.db")
cursor = conexao.cursor()

# Criação da tabela de produtos
cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo TEXT UNIQUE NOT NULL,
    nome TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    preco REAL NOT NULL,
    nivel_minimo INTEGER NOT NULL,
    ativo INTEGER DEFAULT 1
)
""")

# Criacao da tabela de movimentações
cursor.execute("""
CREATE TABLE IF NOT EXISTS movimentacoes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto_id INTEGER NOT NULL,
    tipo TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    data TEXT NOT NULL,
    motivo TEXT,
    FOREIGN KEY (produto_id) REFERENCES produtos (id)
)
""")

conexao.commit()

def adicionar_produtos():
    # Adicionar um novo produto ao estoque.
    print("\n **** Adicionar Produto ****")
    codigo = input("Código do produto: ").strip()
    nome = input("Nome do produto: ").strip()
    quantidade = int(input("Quantidade inicial: "))
    preco = float(input("Preço unitário: "))
    nivel_minimo = int(input("Nível mínimo de estoque: "))

    try:
        cursor.execute("""
        INSERT INTO produtos (codigo, nome, quantidade, preco, nivel_minimo)
        VALUES (?,?,?,?,?)                   
        """, (codigo, nome, quantidade, preco, nivel_minimo))
        conexao.commit()
        print("Produto adicionado com sucesso.")
    except sqlite3.IntegrityError:
        print("Erro: O código do produto já está cadastrado!")

def listar_produtos():
    # Exibe a lista de produtos cadastrados.
    print("\n --- Lista de produtos ---")
    cursor.execute("SELECT id, codigo, nome, quantidade, preco, nivel_minimo, ativo FROM produtos WHERE ativo = 1")
    produtos = cursor.fetchall()

    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        for produto in produtos:
            id_, codigo, nome, quantidade, preco, nivel_minimo, ativo = produto
            print(f"[{id_}]{codigo} - {nome} | Quantidade: {quantidade} | Preço: R${preco:.2f} | Nível Mínimo: {nivel_minimo} ")

def movimentar_estoque():
    # Registra entrada ou saída de produtos no estoque.
    print("\n ****  Movimentação de estoque ****")        
    listar_produtos()
    produto_id = int(input("ID do produto: "))
    tipo = input("Tipo de movimentação (entrada/saida): ").strip().lower()
    quantidade = int(input("Quantidade: "))
    motivo = input("Motivo da movimentação: ").strip()

    cursor.execute("SELECT quantidade FROM produtos WHERE id = ?", (produto_id,))
    resultado = cursor.fetchone()
    if not resultado:
        print("Produto não encontrado.")
        return
    quantidade_atual = resultado[0]

    if tipo == "saida" and quantidade > quantidade_atual:
        print("Erro: Estoque insuficiente!")
        return
    
    nova_quantidade = quantidade_atual + quantidade if tipo == "entrada" else quantidade_atual - quantidade

    cursor.execute("UPDATE produtos SET quantidade = ? WHERE id = ?", (nova_quantidade, produto_id))
    cursor.execute("""
    INSERT INTO movimentacoes (produto_id, tipo, quantidade, data, motivo)
    VALUES (?,?,?, datetime('now'),?)
    """, (produto_id, tipo, quantidade, motivo))
    conexao.commit()
    print("Movimentação registrada com sucesso.")

def menu():
    # Menu principal do sistema.
    while True:
        print("\n ****** Sistema de controle de estoque ******")
        print("1. Adicionar Produto")
        print("2. Listar Produto")
        print("3. Movimentar Estoque")
        print("4. Adicionar Sair")

        escolha = input("Escolha uma opção: ").strip()
        if escolha == "1":
            adicionar_produtos()
        elif escolha == "2":
            listar_produtos()
        elif escolha == "3":
            movimentar_estoque()
        elif escolha == "4":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")
        
if __name__ == "__main__":
    menu()
    conexao.close()