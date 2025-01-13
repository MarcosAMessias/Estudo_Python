import random 

# Categorias com listas de palavras
categorias = {
    "animais":["cachorro","gato","elefante","tigre","jacare"],
    "países":["brasil","canada","argentina","japao","alemanha"],
    "tecnologia":["python","algoritmo","computador","internet","servidor"]
}

def escolher_palavra(categoria):
    """
    Escolhe uma palavra aleatória com base na categoria selecionada.
    """
    return random.choice(categorias[categoria])

def exibir_palavra_oculta(palavra, letras_corretas):
    """
    Exibe a palavra com as letras acertadas reveladas e as outras como "_".
    """
    return " ".join([letra if letra in letras_corretas else "_" for letra in palavra])

def selecionar_categoria():
    """
    Permite que o jogador escolha uma categoria para o jogo.
    """
    print("Categorias disponíveis: ")
    for categoria in categorias:
        print(f"-{categoria}")

    while True:
        escolha = input("Escolha uma categoria: ").lower()
        if escolha in categorias:
            return escolha
        print("Categoria inválida. Tente novamente.")

def selecionar_dificuldade():
    """
    Define o número de tentativas com base no nível de dificuldade escolhido.
    """
    print("\nNíveis de dificuldade:")
    print("\n1 - Fácil (10 tentativas)")
    print("\n2 - Médio (6 tentativas)")
    print("\n3 - Difícil (4 tentativas)")

    while True:
        escolha = input("Escolha um nível de dificuldade (1, 2 ou 3): ").strip()
        if escolha == "1":
            return 10
        elif escolha == "2":
            return 6
        elif escolha == "3":
            return 4
        print("Opção inválida. Escolha 1, 2 ou 3.")

def jogo_da_forca():
    """
    Função principal do jogo da forca com categorias e níveis de dificuldades.
    """
    print("**** Bem-vindo ao Jogo da Forca ****")

    # Escolha da categoria
    categoria = selecionar_categoria()

    # Escolha da categoria e dificuldade
    tentativas_restantes = selecionar_dificuldade()

    # Escolhe a palavra secreta e inicializa variáveis
    palavra_secreta = escolher_palavra(categoria)
    letras_corretas = set()
    letras_erradas = set()

    print(f"\nVocê escolheu a categoria '{categoria}'.")
    print(f"A palavra tem {len(palavra_secreta)} letras.")

    # Loop principal do jogo
    while tentativas_restantes > 0:
        # Exibe o estado atual da palavra e informações
        print("\nPalavra:",exibir_palavra_oculta(palavra_secreta, letras_corretas))
        print(f"Letras erradas: {', '.join(letras_erradas) if letras_erradas else 'Nenhuma'}")
        print(f"Tentativas restantes: {tentativas_restantes}")

        # Solicita ao jogador uma letra
        tentativa = input("Adivinhe uma letra: ").strip().lower()

        # Verifica se a entrada é válida
        if len(tentativa) != 1 or not tentativa.isalpha():
            print("Entrada inválida. Digite apenas uma letra.")
            continue

        # Verifica se a letra já foi tentada
        if tentativa in letras_corretas or tentativa in letras_erradas:
            print("Você já tentou essa letra . Tente outra.")
            continue

        # Processa a tentativa do jogador
        if tentativa in palavra_secreta:
            letras_corretas.add(tentativa)
            print("Boa! A letra está na palavra.")
        else:
            letras_erradas.add(tentativa)
            tentativas_restantes -= 1
            print("Que pena! A letra não está na palavra.")

        # Verifica se o jogador adivinhou a palavra inteira
        if all(letra in letras_corretas for letra in palavra_secreta):
            print("\nParabéns! Você acertou a palavra:", palavra_secreta)
            break
    else:
        # Executado se o jogador não adivinhar antes de esgotar as tentativas
        print("\nVocê perdeu! A palavra era:", palavra_secreta)

if __name__ == "__main__":
    jogo_da_forca()