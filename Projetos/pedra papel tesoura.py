import random 

def obter_escolha_usuario():
    escolha = input("Escolha Pedra, Papel ou Tesoura: ").lower()
    while escolha not in ['pedra', 'papel', 'tesoura']:
        escolha = input("Escolha inválida. Escolha Pedra, Papel ou Tesoura:\n").lower
    return escolha 

def obter_escolha_computador():
    escolhas = ['pedra', 'papel', 'tesoura']
    return random.choice(escolhas)

def determinar_vencedor(escolha_usuario, escolha_computador):
    if escolha_usuario == escolha_computador:
        return "Empate"
    elif (escolha_usuario == 'pedra' and escolha_computador == 'tesoura') or \
        (escolha_usuario == 'papel' and escolha_computador == 'pedra') or \
        (escolha_usuario == 'tesoura' and escolha_computador == 'papel'):
        return "Você venceu!"
    else:
        return "O computador venceu."
    
def jogar():
    jogar_novamente = 'sim'
    while jogar_novamente == 'sim':
        escolha_usuario = obter_escolha_usuario()
        escolha_computador = obter_escolha_computador()
        print(f"Você escolheu: {escolha_usuario.capitalize()}")
        print(f"O computador escolheu: {escolha_computador.capitalize()}")
        resultado = determinar_vencedor(escolha_usuario, escolha_computador)
        print(resultado)
        jogar_novamente = input("Quer jogar novamente? (sim/não): ").lower()
    print("Obrigado por jogar!")

jogar()