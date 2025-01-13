import random

# Lista de palavras para o jogo
palavras = ["python","tecnologia","desenvolvimento","algoritmo","programacao"]

def escolher_palavras():
    """
    Escolhe uma palavra aleatória da lista de palavras.
    """
    return random.choice(palavras)

def exibir_palavra_oculta(palavra, letras_corretas):
    """
    Retorna a palavra com as letras adivinhadas reveladas e as não adivinhadas substituídas por "_".
    """
    return " ".join([letra if letra in letras_corretas else "_" for letra in palavra])

def jogo_da_forca():
    """
    Função principal do jogo da forca.
    Gerencia o fluxo do jogo, com tentativas, letras adivinhadas e resultado final.
    """
    print(" ***** Bem-vindo ao Jogo da Forca *****")

    # Escolhe uma palavra aleatória e inicializa variáveis
    palavra_secreta = escolher_palavras()
    letras_corretas = set() # Letras que o jogador acertou
    letras_erradas = set() # Letras que o jogador errou
    tentativas_restantes = 6 # Números de tentativas permitidas

    print("\nA palavra tem", len(palavra_secreta), "letras.")

    # Loop principal do jogo
    while tentativas_restantes > 0:
        # Exibe o estado atual da palavra
        print("\nPalavra:",exibir_palavra_oculta(palavra_secreta, letras_corretas))
        print(f"Letras Erradas: {', '.join(letras_erradas) if letras_erradas else 'Nenhuma'}")
        print(f"Tentativas restantes: {tentativas_restantes}")

        # Solicita ao jogador uma letra
        tentativa = input("Adivinhe uma letra: ").strip().lower()

        # Verifica se a entrada é válida
        if len(tentativa) != 1 or not tentativa.isalpha():
            print("Entrada inválida. Digite apenas uma letra.")
            continue

        # Verifica se a letra já foi tentada]
        if tentativa in letras_corretas or tentativa in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
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
            print("\nParabéns! Você acertou a palavra: ", palavra_secreta)
            break
    
    else: 
        # Executado se o jogador não adivinhar antes de esgotar as tentativas
        print("\nVocê perdeu! A palavra era:", palavra_secreta)

if __name__ == "__main__":
    jogo_da_forca()

