#  Metodos para string
mensagem = 'Eu adoro comida caseira'
#           0123456789
print(mensagem.upper()) # Imprime em caixa alta

#lower caixa baixa
#capitalize primeira letra em maiuscula

print(mensagem.find('c'))  # o primeiro c está na posição 9 do índice
print(mensagem.find('adoro')) # a palavra inicia no índice 3
print(mensagem.find('aDoro')) # -1 significa que não achou
print(mensagem.replace('a','e')) # substitui o a pelo e
print(mensagem.replace('caseira','feita em casa')) # troca caseira por feito em casa
print(mensagem.strip())# retira os campos em branco antes e ao final da frase

