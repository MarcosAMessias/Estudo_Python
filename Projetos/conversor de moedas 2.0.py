import requests

# Função para obter a taxa de câmbio da API 1 (Exchangerat.host)
def obter_taxa_de_cambio_api1(moeda_origem, moeda_destino):
    url = f"https://api.exchangerate.host/convert?from={moeda_origem}&to={moeda_destino}"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        if 'result' in dados:
            return dados['result']
    except requests.exceptions.RequestException as e:
        print(f"Erro na API 1: {e}")

    return None

# Função para obter a taxa de câmbio da API 2 (exemplo: Open Exchange Rates)
def obter_taxa_de_cambio_api2(moeda_origem, moeda_destino, api_key="AQUI RETIREI A MINHA API"):
    url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        if 'rates' in dados:
            taxa_origem = dados['rates'].get(moeda_origem)
            taxa_destino = dados['rates'].get(moeda_destino)
            if taxa_origem and taxa_destino:
                return taxa_destino / taxa_origem
    except requests.exceptions.RequestException as e:
        print(f"Erro na API 2: {e}")
    return None

# Função principal para obter a taxa de câmbio
def obter_taxa_de_cambio(moeda_origem, moeda_destino):
    # Tenta usar a API 1 primeiro 
    taxa = obter_taxa_de_cambio_api1(moeda_origem, moeda_destino)
    if taxa is not None:
        print("Taxa obtida da API 1.")
        return taxa
    
    # Se a API 1 falhar, tenta usar a API 2
    taxa = obter_taxa_de_cambio_api2(moeda_origem, moeda_destino)
    if taxa is not None:
        print("Taxa obtida da API 2.")
        return taxa
    
    # Se ambas falharem 
    print("Não foi possível obter a taxa de câmbio de nenhuma API.")
    return None

# Exemplo de uso
def conversor_de_moedas():
    moeda_origem = input("Digite o código de origem (ex. BRL, USD, EUR): ").strip().upper()
    moeda_destino = input("Digite o código da moeda de destino (ex. BRL, USD, EUR): ").strip().upper()
    try:
        valor = float(input(f"Digite o valor em {moeda_origem} que deseja converter: "))
    except ValueError:
        print("Valor inválido! Tente novamente com um número válido.")
        return
    
    taxa = obter_taxa_de_cambio(moeda_origem, moeda_destino)
    if taxa is not None:
        valor_convertido = valor * taxa
        print(f"{valor:.2f}{moeda_origem} equivale a {valor_convertido:.2f}{moeda_destino}.")
    else:
        print("Conversão não pôde ser realizada.")

if __name__ == "__main__":
    conversor_de_moedas()  