import base64 # Biblioteca para operações de codificação/decodificação em Base64
from cryptography.fernet import Fernet # Biblioteca para criptografia simétrica (Fernet)

# Função para exibir o menu principal e capturar a escolha do usuário
def exibir_menu():
    """
    Exibe o menu principal com as opcões disponíveis.
    Retorna a escolha do usuário como uma string.
    """
    print("\n ***** Menu de Criptografia ******")
    print("1. Cifra de César")
    print("2. Base64")
    print("3. Criptografia Simétrica (AES)")
    print("4. Sair")
    escolha = input("Escolha uma opção (1-4):\n").strip()
    return escolha

# Função para realizar a Cifra de César
def cifra_de_cesar(texto, chave, operacao):
    """
    Aplica a Cifra de César para criptografar um texto.
    :param texto: Texto de entrada
    :param chave: Número de posições para deslocar os caracteres
    :param operacao: 'criptografar' ou 'descriptografar'
    :return: Texto resultante após a operação
    """
    resultado = "" # Armazena o texto processado
    deslocamento = chave if operacao == 'criptografar'else - chave # Define o deslocamento
    for char in texto: # Itera sobre cada caractere do texto
        if char.isalpha(): # Verifica se o caracter é uma letra
            limite = ord('A') if char.isupper() else ord('a') # Determina se é maiúscula ou minúscula
            # Calcula o novo caractere após o deslocamento circular
            novo_char = chr((ord(char) - limite + deslocamento) % 26 + limite)
            resultado += novo_char # Adiciona o novo caractere ao resultado
        else:
            resultado += char # Mantém caracteres não alfabéticos inalterados
    return resultado

# Função para realizar codificação e decodificação em Base64
def base64_operacao(texto, operacao):
    """
    Codifica ou decodifica texto usando Base64.
    :param texto: Texto de entrada 
    :param operacao: 'criptografia' ou 'descriptografia'
    :return: Texto resultante após a operação
    """
    if operacao == 'criptografar':
        # Codifica o texto em Base64
        return base64.b64encode(texto.encode()).decode()
    elif operacao == 'descriptografar':
        # Decodifica o texto de Base64
        try:
            return base64.b64decode(texto).decode()
        except Exception as e:
            return f"Erro ao descriptografar: {e}"
        
# Função para gerar uma chave para o algoritmo Fernet
def gerar_chave():
    """
    Gera uma chave segura para uso com o algoritmo Fernet.
    Retorna a chave gerada como string.
    """
    return Fernet.generate_key().decode()

# Função para realizar criptografia e descriptografia simétrica com Fernet
def criptografia_simetrica(texto, chave, operacao):
    """
    Realiza criptografia ou descriptografia usando o algoritmo Fernet.
    :param texto: Texto de entrada 
    :param chave: Chave de criptografia
    :param operação: 'criptografar' ou 'descriptografar'
    :return: Texto resultante após a operação
    """
    try:
        fernet = Fernet(chave.encode()) # Cria o objeto Fernet com a chave fornecida
        if operacao == 'criptografar':
            # Criptografa o texto
            return fernet.encrypt(texto.encode()).decode()
        elif operacao == 'descriptografar':
            # Descriptografa o texto
            return fernet.decrypt(texto.encode()).decode()
    except Exception as e:
        return f"Erro: {e}"
    
# Função principal que gerencia o fluxo do programa
def main():
    """
    Função principal para interação com o usuário.
    Gerencia a escolha de algoritmos e operações.
    """
    print("***** Sistema de Criptografia ******") # Título do programa
    while True:
        escolha = exibir_menu() # Exibe o menu e captura a escolha
        if escolha == "1":
            print("\n****** Cifra de César *******")
            texto = input("Texto: ")
            chave = int(input("Chave (número): "))
            operacao = input("Operação (criptografia/descriptografar): ").strip().lower()
            print("Resultado:", cifra_de_cesar(texto, chave, operacao))
        elif escolha == "2":
            print("\n=== Base64 ===")
            texto = input("Texto: ")
            operacao = input("Operação (criptografar/descriptografar): ").strip().lower()
            print("Resultado:", base64_operacao(texto, operacao))
        elif escolha == "3":
            print