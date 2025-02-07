def palindromo(palavra):
    # Converte a palavra para minúscula para garantir que a verificação não seja sensível a maiúscula/minuscula
    palavra = palavra.lower()

    # Verifica se a palavra é igual à sua versão invertida
    return palavra == palavra[::-1]

# Testando a função 
# A função deve retornar True, pois "arara" lida de trás para frente é "arara"
print(palindromo("arara")) # Saída: True

# A função deve retornar False, pois "python" lida de trás para frente é "nohtyp"
print(palindromo("python")) # Saída: False