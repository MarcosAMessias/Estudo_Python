# Função para converter temperatura entre Celsius, Fahrenheit e Kelvin
def converter_temperatura(valor, unidade_origem, unidade_destino):
    if unidade_origem == "C" and unidade_destino == "F":
        return valor * 9 / 5 + 32 # Celsius para Fahrenheit 
    elif unidade_origem == "F" and unidade_destino == "C":
        return (valor - 32) * 5 / 9 # Fahrenheit para Celsius 
    elif unidade_origem == "C" and unidade_destino == "K":
        return valor + 273.15  # Celsius para Kelvin 
    elif unidade_origem == "K" and unidade_destino == "C":
        return valor - 273.15  # Kelvin para Celsius
    else:
        return "Conversão de temperatura não suportada."
    
# Função para converter distância entre diferentes unidades (km, milhas, metros e centimetros)
def converter_distancia(valor, unidade_origem, unidade_destino):
    if unidade_origem == "km" and unidade_destino == "mi":
        return valor * 0.621371 # Quilômetros para Milhas
    elif unidade_origem == "mi" and unidade_destino == "km":
        return valor / 0.621371 # Milhas para Quilômetros 
    elif unidade_origem == "m" and unidade_destino == "cm":
        return valor * 100 # Metros para Centímetros
    elif unidade_origem == "cm" and unidade_destino == "m":
        return valor / 100 # Centímetros para Metros
    else:
        return "Conversão de distância não suportada."
        
# Função para converter peso entre quilogramas, libras e gramas
def converter_peso(valor, unidade_origem, unidade_destino):
    if unidade_origem == "kg" and unidade_destino == "lb":
        return valor * 2.20462 # Quilogramas para Libras
    elif unidade_origem == "lb" and unidade_destino == "kg":
        return valor / 2.20462 # Libras para Quilogramas
    elif unidade_origem == "g" and unidade_destino == "kg":
        return valor / 1000 # Gramas para quilogramas
    elif unidade_origem == "kg" and unidade_destino == "g":
        return valor * 1000 # Quilogramas para gramas
    else:
        return "Conversão de peso não suportadada."
    
# Função para converter velocidade entre km/h,  m/s e mi/h
def converter_velocidade(valor, unidade_origem, unidade_destino):
    if unidade_origem == "km/h" and unidade_destino == "m/s":
        return valor / 3.6 # Quilômetros por hora para metros por segundo 
    elif unidade_origem == "m/s" and unidade_destino == "km/h":
        return valor * 3.6 # Metros por segundo para quilometros por hora
    elif unidade_origem == "mi/h" and unidade_destino == "km/h":
        return valor * 1.60934 # Milhas por hora para quilometros por hora
    elif unidade_origem == "km/h" and unidade_destino == "mi/h":
        return valor / 1.60934 # Quilômetros por hora para milhas por hora
    else:
        return "Conversão de velocidade não suportada."

# Função principal que exibe o menu e gerencia a interação com o usuário
def main():
    print("=== Conversor de Unidades ===")
    print("Escolha o tipo de conversão:")
    print("1. Temperatura \U0001F321 (Celsius, Fahrenheit, Kelvin )")
    print("2. Distância \U0001F6E3  (km, mi, m, cm)")
    print("3. Peso \u2696 (kg, lb, g)")
    print("4. Velocidade \U0001F3C3 (km/h, m/s, mi/h)")

    # Captura a escolha do tipo de conversão 
    escolha = input("Digite o número correspondente ao tipo de conversão: ").strip()

    if escolha == "1": # Conversão de temperatura
        valor = float(input("Digite o valor a ser convertido: "))
        unidade_origem = input("Digite a unidade de origem (C,F, K):").strip().upper()
        unidade_destino = input("Digite a unidade de destino (C, F, K): ").strip().upper()
        resultado = converter_temperatura(valor, unidade_origem, unidade_destino)
    elif escolha == "2": # Conversão de distância
        valor = float(input("Digite o valor a ser convertido: "))
        unidade_origem = input("Digite a unidade de origem (km, mi, m, cm):").strip()
        unidade_destino = input("Digite a unidade de destino (km, mi, m ,cm): ").strip()
        resultado = converter_distancia(valor, unidade_origem, unidade_destino)
    elif escolha == "3": # Conversão de peso
        valor = float(input("Digite  o valor a ser convertido: "))
        unidade_origem = input("Digite a unidade de origem (kg, lb, g): ").strip()
        unidade_destino = input("Digite a unidade de destino (kg, lb, g): ").strip()
        resultado = converter_peso(valor, unidade_origem, unidade_destino)
    elif escolha == "4": # Conversão de velocidade
        valor = float(input("Digite o valor a ser convertido: "))
        unidade_origem = input("Digite a unidade de origem (km/h, m/s, mi/h): ").strip()
        unidade_destino = input("Digite a unidade de destino (km/h, m/s, mi/h): ").strip()
        resultado = converter_velocidade(valor, unidade_origem, unidade_destino)
    else:
        resultado = "Opção inválida." # Caso o usuário escolha uma opção inexistente

    # Exibe o resultado da conversão 
    print(f"\nResultado: {resultado}")

# Executa o programa apenas se ele for chamado diretamente
if __name__ == "__main__":
    main()
