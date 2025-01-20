import networkx as nx # Biblioteca para criar e manipular grafos
import mathplotlib.pyplot as plt # Biblioteca para visualização de gráficos

# Inicialização do grafo que representará a topologia da rede
topologia =  nx.Graph()

def adicionar_dispositivo():
    """
    Docstring 
    Adiciona um dispositivo à topologia da rede.
    """
    dispositivo = input("Nome do dispositivo: ").strip() # Solicita o nome do dispositivo
    ip = input("Endereço IP do dispositivo: ").strip() # Solicita o IP do dispositivo

    # Verifica se o dispositivo ou IP já existe
    if dispositivo in topologia.nodes or any(data['ip'] == ip for _, data in topologia.nodes(data=True)):
        print("Erro: Dispositivo ou IP já existe na rede.")
    else:
        # Adiciona o dispositivo ao grafo com o ip como atributo
        topologia.add_node(dispositivo, ip=ip)
        print(f"Dispositivo '{dispositivo}' com IP '{ip}' adicionado com sucesso!")

def conectar_dispositivos():
    """
    Cria uma conexão (link) entre dois dispositivos na topologia
    """
    origem = input("Dispositivo de origem: ").strip() # Solicita o dispositivo de origem
    destino = input("Dispositivo de destino: ").strip() # Solicita o dispositivo de destino
    
    # Verfica se ambos os dispositivos existem
    if origem in topologia.nodes and destino in topologia.nodes:
        topologia.add_edge(origem, destino) # Adiciona uma conexão bidirecional
        print(f"Conexão criada entre '{origem}' e '{destino}'.")
    else:
        print("Erro: Um ou ambos os dispositivos não existem.")

def exibir_topologia():
    """
    Exibe a topologia da rede com seus dispositivos e conexões.
    """
    print("nDispositivos na Rede:")
    for dispositivo, dados in topologia.nodes(data=True):
        print(f"- {dispositivo} (IP:{dados['ip']})")

    print("\nConexões: ")
    for origem, destino in topologia.edges:
        print(f"- {origem} <--> {destino}")

    # Visualiza o grafo da rede
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(topologia) # Calcula a disposição dos nós
    nx.draw(topologia, pos, with_labels=True, node_size=500, node_color="lightblue")
    labels = nx.get_node_attributes(topologia, 'ip')
    nx.draw_networkx_labels(topologia, pos, labels=labels, font_color="darkgreen")
    plt.title("Topologia da Rede")
    plt.show()

def enviar_pacote():
    """
    Simula o envio de um pacote entre dois dispositivos.
    """
    origem = input("Dispositivo de origem: ").strip() # Solicita o dispositivo de origem
    destino = input("Dispositivo de destino: ").strip() # Solicita o dispositivo de destino

    # Verifica se ambos os dispositivos existem
    if origem in topologia.nodes and destino in topologia.nodes:
        try:
            # Calcula o menor caminho entre os dispositivos
            caminho = nx.shortest_path(topologia, source=origem, target=destino)
            print(f"Pacote enviado de '{origem}' para '{destino}' via caminho: {' -> '.join(caminho)}")
        except nx.NetworkXNoPath:
            # Caso não haja caminho entre os dispositivos
            print(f"Erro: Não há caminho entre '{origem}' e '{destino}'.")
    else:
        print("Erro: Um ou ambos dispositivo não existem.")

def main():
    """
    Função principal para gerenciar o fluxo do programa.
    """
    print("Bem-vindo ao Simulador de Rede de Computadores!")

    while True:
        # Menu de opções para o usuário
        print("\nMenu:")
        print("1. Adicionar dispositivo")
        print("2. Conectar dispositivo")
        print("3. Exibir topologia")
        print("4. Enviar pacote")
        print("5. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_dispositivo()
        elif opcao == "2":
            conectar_dispositivos()
        elif opcao == "3":
            exibir_topologia()
        elif opcao == "4":
            enviar_pacote()
        elif opcao == "5":
            print("Encerrando o simulador...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()