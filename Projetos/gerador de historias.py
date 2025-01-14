import random 

# Função para gerar uma história aleatória
def gerar_historia():
    personagens = [
        "\U0001F9B8 Um herói perdido ",
        "\U0001F9D9 Uma bruxa má ",
        "\U0001F9D1 Um cientista maluco ",
        "\U0001F920 Um cavaleiro valente ",
        "\U0001F47D Um alienígena curioso ",
        "\U0001F575 Um detetive improvisado "
    ]
    
    cenarios = [
        "em uma floresta encantada",
        "no fundo do oceano",
        "em uma cidade abandonada",
        "em uma casa assombrada",
        "no espaço sideral",
        "em uma vila medieval"
    ]

    acontecimentos = [
        "descobriu um artefato mágico",
        "encontrou um mapa do tesouro",
        "enfrentou um exército inimigo",
        "salvou uma vila de um ataque",
        "descobriu um segredo do passado",
        "invocou poderes desconhecidos"
    ]

    final = [
        " e viveu feliz para sempre.",
        " mas precisou tomar uma difícil decisão.",
        " e mudou para sempre sua vida.",
        " e se tornou uma lenda.",
        " e conseguiu a paz.",
        " mas precisou lutar muito."
    ]

    # Escolhendo aleatoriamente cada parte da história
    personagem = random.choice(personagens)
    cenario = random.choice(cenarios)
    acontecimento = random.choice(acontecimentos)
    fim = random.choice(final)

    # Montando a história
    historia = f"{personagem}{cenario}{fim}"
    return historia

# Função para perguntar ao usuário se quer gerar uma nova história
def pedir_historias():
    while True:
        resposta = input("Deseja gerar uma história aleatória? (sim/não): ").strip().lower()
        if resposta == 'sim':
            historia = gerar_historia()
            print("\nHistória Gerada:\n", historia)
        elif resposta == 'não':
            print("Até a próxima!")
            break
        else:
            print("Por favor, responda com 'sim' ou 'não'.")

# Início do programa
if __name__ == "__main__":
    print("Bem-vindo ao Gerador de Histórias Aleatórias!")
    pedir_historias()
    