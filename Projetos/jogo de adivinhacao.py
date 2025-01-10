import random # Importa o módulo random para gerar números aleatórios

def jogo_adivinhacao():
    """
    Função principal do jogo de adivinhação.
    Permite ao jogador escolher um nível de dificuldade e adivinhar um número secreto.
    Retorna o número de tentativas do jogador.
    """

    print("=== Jogo de adivinhação ===")
    print("Bem-vindo ao jogo! Você precisa adivinhar o número secreto.")

    # Solicita o nível de dificuldade ao jogador
    print("\nEscolha um nível de dificuldade:")
    print("1. Fácil (1-50)")
    print("2. Médio (1-100)")
    print("3. Difícil (1-500)")

    while True:
        try:
            #Lê a escolha do jogador para definir o nível de dificuldade
            nivel = int(input("Digite o número correspondente ao nível de dificuldade: "))
            if nivel == 1:
                limite_inferior, limite_superior = 1, 50 # Intervalo para nível fácil
                break
            elif nivel == 2:
                limite_inferior, limite_superior = 1, 100 # Intervalo para nível médio
                break
            elif nivel == 3:
                limite_inferior, limite_superior = 1, 500 # Intervalo para o nível difícil
                break
            else:
                print("Por favor, escolha uma opção válida (1, 2 ou 3).")
        except ValueError: 
            print("Por favor, insira um número válido.")

    # Gera um número secreto aleatório dentro do intervalo escolhido
    numero_secreto =  random.randint(limite_inferior, limite_superior)
    tentativas = 0 # Inicializa o contador de tentativas

    print(f"\nEstou pensando em um número entre {limite_inferior} e {limite_superior}.")

    # Loop para o jogador adivinhar o número
    while True:
        try:
            # Solicita o palpite do jogador
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1 # incrementa o contador de tentativas

            # Dá dicas ao jogador com base no palpite
            if palpite < numero_secreto:
                print("Muito baixo! \U0001F447 Tente novamente.\U0001F649")
            elif palpite > numero_secreto:
                print("Muito alto! \U0001F446 Tente novamente.\U0001F648")
            else:
                # O jogador acertou 
                print(f"Parabéns! \U0001F3AF Você acertou o número {numero_secreto} em {tentativas} tentativas.")
                return tentativas # Retorna o número de tentativas ao final
        except ValueError:
            # Trata entradas inválidas (exemplo: texto ou caracteres especiais)
            print("Vamos tentar com um número válido.")

def main():
    """
    Função principal que gerencia o fluxo do jogo:
    - Inicia o jogo
    - Armazena e exibe o ranking de tentativas
    - Permite jogar novamente
    """

    ranking = [] # Lista para armazenar as pontuações (menor número de tentativas)

    while True:
        # Chama o jogo e armazena o número de tentativas do jogador
        tentativas = jogo_adivinhacao()
        ranking.append(tentativas) # Adiciona as tentativas ao ranking

        # Exibe o ranking atualizado, ordenado do menor para o maior número de tentativas
        print("\n=== Ranking de menor número de tentativas ===")
        for i, tentativas in enumerate(sorted(ranking), start=1):
            print(f"{i}. {tentativas} tentativas(s)")

        # Pergunta ao jogador se deseja jogar novamente 
        jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").strip().lower()
        if jogar_novamente != 's': # Sai do loop se o jogador não quiser continuar
            print("Obrigado por jogar! \U00002764 Até a próxima.")
            break
if __name__ == "__main__":
    # Ponto de entrada do programa. O jogo só inicia se o arquivo for executado diretamente.
    main()

