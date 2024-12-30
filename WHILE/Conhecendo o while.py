'''
 Conhecendo o while: loop dependente de uma condição TRUE
 Criando uma promoção para um produto no valor de R$ 100
 '''
valor = 100
dia = 1
while valor >= 20:
    dia += 1
    print(f'no dia {dia}, o valor é {valor}')
    valor -= 5

