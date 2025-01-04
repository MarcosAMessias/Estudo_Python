valor = int(input('Digite o valor do seu produto em R$:\n'))
while valor > 20:
    valor = (valor * 0.10) + valor
    print(f'Ovalor final do seu produto será de R${valor:.2f}')
    break