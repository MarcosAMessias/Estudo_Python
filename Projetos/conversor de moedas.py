import requests # Biblioteca para fazer requisições HTTP
# Função para obter a taxa de câmbio atual usando API
def obter_taxa_de_cambio(moeda_origem, moeda_destino):
    """
    Obtém a taxa de câmbio entre a moeda de origem e a moeda de destino.
    Utiliza a API gratuita de câmbio da exchangerate.host.
    """
    url = f"https://api.exchangerate.host/convert?from={moeda_origem}&to={moeda_destino}"
    try:
        resposta = requests.get(url) # Faz a requisição à API
        resposta.raise_for_status() # Verifica se a requisição foi bem-sucedida
        dados = resposta.json() # Converte a resposta para o formato JSON

        # Verifica se o JSON contém a taxa de câmbio
        if 'result' in dados:
            return dados['result'] # Retorna a taxa de câmbio
        else:
            print("A API não retornou a taxa de câmbio esperada.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
        return None

# Função principal para o conversor
def conversor_de_moedas():
    print("\U0001F4B5 \U0001F4B4 \U0001F4B6 Conversor de Moedas \U0001F4B0 \U0001F4B3 \U0001FA99")
    # Solicita ao usuário as informações necessárias
    moeda_origem = input("Digite o código da moeda de origem (ex: BRL, USD, EUR: )").strip().upper()
    moeda_destino = input("Digite o código da moeda de destino (ex. BRL, USD, EUR): ").strip().upper()
    try:
        valor = float(input(f"Digite o valor em {moeda_origem} que deseja converter: "))
    except ValueError:
        print("Valor inválido! Tente novamente com um número válido.")
        return
    
    # Obtém a taxa de câmbio 
    taxa_de_cambio = obter_taxa_de_cambio(moeda_origem, moeda_destino)
    if taxa_de_cambio is None:
        print("Não foi possível obter a taxa de câmbio. Tente novamente mais tarde.")
        return
    
    # Realiza a conversão 
    valor_convertido = valor * taxa_de_cambio

    # Exibe o resultado formatado
    print(f"\***** Conversão *****")
    print(f"{valor:.2f} {moeda_origem} é equivalente a {valor_convertido:.2f} {moeda_destino}.")
    print(f"Taxa de câmbio utilizada: 1 {moeda_origem} = {taxa_de_cambio:.4f} {moeda_destino}.")

# Ponto de entrada do programa
if __name__ == "__main__":
    while True:
        conversor_de_moedas() # Executa o conversor
        opcao = input("\nDeseja realizar outra conversão? (s/n): ").strip().lower()
        if opcao != 's':
            print("Obrigado por usar o Conversor de Moedas! Até mais!")
            break