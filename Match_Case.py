# Match Case
def identificando_tipo(valor):
    match valor:
        case int():
            print("É um número inteiro.")
        case float():
            print("É um número flutuante.")
        case str():
            print("É uma string (texto).")
        case list():
            print("É uma lista.")
        case _:
            print("Tipo desconhecido.")

identificando_tipo(41) # É um número inteiro
identificando_tipo("Olá Mundo") # É uma string
identificando_tipo([1, 2, 3]) # É uma lista
identificando_tipo(4.1) # É um número flutuante
