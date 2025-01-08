import random
import string

def gerar_senha(tamanho, incluir_maiusculas = True, incluir_numeros = True, incluir_especiais = True):
    # Conjunto básico: letras minúsculas
    caracteres = string.ascii_lowercase

    #Adiciona outros conjuntos com base nas preferências do usuário
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_especiais:
        caracteres += string.punctuation

    # Gera a senha
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    print("=== \U0001F512 Gerador de Senhas Seguras \U0001F511 ===")
    try:
        tamanho = int(input("Digite o comprimento da senha desejada (ex: 12):\n"))
        incluir_maiusculas =input("Incluir letras maiúsculas? (s/n): \n").strip().lower() =='s'
        incluir_numeros = input("Incluir números? (s/n): \n").strip().lower() == 's'
        incluir_especiais = input("Incluir caracteres especiais? (s/n): \n").strip().lower() =='s'

        # Gera a senha com as preferências do usuário
        senha = gerar_senha(tamanho, incluir_maiusculas, incluir_numeros, incluir_especiais)
        print(f"\nSua senha gerada: {senha}")
    except ValueError:
        print("Por favor, insira um número válido para o comprimento da senha.")
    finally:
        print('Obrigado por usar o gerador de senhas \u263A')

if __name__ == "__main__":
    main()