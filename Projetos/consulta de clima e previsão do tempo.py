import requests # Biblioteca para fazer requisições HTTP
import os # Para acessar variáveis de ambiente (se necessário)
from dotenv import load_dotenv # Biblioteca para carregar variáveis de ambiente (opcional)

# Carrega as variáveis de ambiente do arquivo .env (se existir)
load_dotenv()

# Substitua pela sua chave de API do OpenWeatherMap
API_KEY = os.getenv("OPENWEATHER_API_KEY") or "colocar a chave aqui"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def obter_dados_climaticos(cidade):
    """
    Faz uma chamada para a API do OpenWeatherMap e retorna os dados climáticos da cidade.
    """
    try:
        # Define os parâmetros da requisição
        parametros = {
            "q":cidade, # Nome da cidade
            "appid":API_KEY, # Chave de api
            "units":"metric", # Unidade de medida (Celsius)
            "lang":"pt_br" # Idioma da descrição do clima
        }

        # Faz a requisição GET para a API
        resposta = requests.get(BASE_URL, params=parametros)
        resposta.raise_for_status() # Lança um erro se a resposta não for bem-sucedida

        # Retorna os dados no formato JSON
    except requests.exceptions.HTTPError as erro_http:
        print(f"Erro HTTP: {erro_http}")
    except requests.exceptions.RequestException as erro_requisicao:
        print(f"Erro na requisição: {erro_requisicao}")
    return None

def exibir_clima(dados):
    """
    Exibe as informações climáticas de forma amigável ao usuário.
    """
    if dados:
        # Extrai as infos principais
        cidade = dados["name"]
        pais = dados["sys"]["country"]
        temperatura = dados["main"]["temp"]
        sensacao_termica = dados["main"]["temp"]
        clima = dados["weather"][0]["description"]
        umidade = dados["main"]["humidity"]
        vento = dados["wind"]["speed"]

        # Exibe os dados formatados
        print("\n ---- Dados Climáticos ----")
        print(f"Cidade: {cidade}, {pais}")
        print(f"Temperatura: {temperatura}ºC")
        print(f"Sensação Térmica: {sensacao_termica}ºC")
        print(f"Condições: {clima}")
        print(f"Umidade: {umidade}%")
        print(f"Velocidade do Vento: {vento} m/s")
    else:
        print("Não foi possível obter os dados climáticos. Verifique o nome da cidade ou sua conexão com a internet.")

def main():
    """
    Função principal que gerencia a interação com o usuário.
    """
    print("***** Consulta de Clima e Previsão do Tempo ******")
    while True:
        cidade = input("\nDigite o nome da cidade (ou 'sair' para encerrar): ").strip()
        if cidade.lower() == "sair":
            print("Encerrando o aplicativo. Até mais!")
            break
        # Obtém os dados climáticos da cidade 
        dados_climaticos = obter_dados_climaticos(cidade)

        # Exibe os dados 
        exibir_clima(dados_climaticos)

if __name__ == "__main__":
    main()