def calc():
    while True:
        try:
            entrada1 = float(input('Digite o primeiro valor: \n'))
            entrada2 = float(input("Digite o segundo número: \n"))
            break # Sai do loop se os inputs forem válidos
        except ValueError:
            print('Por favor, insira apenas números. \U0001f91a')
    calculadora(entrada1, entrada2)

def calculadora(entrada1, entrada2):
    print(f'A soma é: {entrada1 + entrada2}')
    print(f'A subtração é: {entrada1 - entrada2}')
    print(f'A multiplicação é: {entrada1 * entrada2}')
    try:
        print(f'A divisão é:{entrada1 / entrada2}')
    except ZeroDivisionError:
        print('Não consigo dividir por Zero. \U0001f6ab')
    finally:
        print('Obrigado por usar este aplicativo de calculadora! \U0001F609')

    if __name__ == "__main__":
        calc()
calc()