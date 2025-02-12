import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0 
    print("Bem-vindo ao jogo de adivinhação")
    print("Eu escolhi um número entre 1 a 100. Tente adivinhar.")

    while True:
        palpite = int(input("Digite seu palpite: "))
        tentativas +=1

        if palpite < numero_secreto:
            print("Muito baixo. Tente novamente.")
        elif palpite > numero_secreto:
            print("Muito alto. Tente novamente.")
        else:
            print(f"Parabéns! Você adivinhou o número em {tentativas} tentativas.")
            break

jogo_adivinhacao()