import pandas as pd # Biblioteca para manipulação de dados (DataFrames)
import matplotlib.pyplot as plt # Biblioteca para geração de gráficos

def carregar_arquivo():
    """
    Carrega um arquivo CSV ou Excel selecionado pelo usuário.
    Retorna o DataFrame com os dados carregados.
    """

    while True:
        try:
            # Solicita ao usuário o caminho do arquivo
            caminho = input("Informe o caminho do arquivo (CSV ou Excel): ").strip()
            # Verifica se o arquivo é CSV
            if caminho.endswith('.csv'):
                dados = pd.read_csv(caminho)
            # Verifica se o arquivo é Excel
            elif caminho.endswith('.xlsx'):
                dados = pd.read_excel(caminho)
            else:
                # Levanta um erro se o formato for inválido
                raise ValueError("Formato de arquivo inválido. Use .csv ou .xlsx.")
            print("\nArquivo carregado com sucesso!") # Confirmação de carregamento
            return dados # Retorna o DataFrame carregado
        except Exception as e:
            # Mostra mensagens de erro caso o carregamento falhe
            print(f"Erro ao carregar o arquivo: {e}")
            print("Tente novamente. \n")
def validar_dados(dados):
    # Valida o DataFrame, exibindo informações sobre valores ausentes ou inválidos.
    print("\nValidação dos Dados:")
    #Exibe informações gerais do DataFrame, como colunas e tipos de dados
    print("Informações gerais:")
    print(dados.info())
    # Exibe a quantidade de valores ausentes em cada coluna
    print("\nValores ausentes por coluna:")
    print(dados.isnull().sum())

def calcular_estatisticas(dados):
    # Calcula e exibe estatísticas descritivas básicas para colunas numéricas.
    print("\nEstatísticas Descritivas:")
    # Usa o método describe() para calcular estatísticas como média, desvio padrão, etc.
    estatisticas = dados.describe()
    print(estatisticas) # Exibe as estatísticas no console 
    return estatisticas # Retorna o DataFrame com as estatísticas

def gerar_graficos(dados):
    # Gera gráficos básicos com base nos dados fornecidos.
    while True:
        # Menu de opções para seleção de tipo de gráfico
        print("\nOpções de Gráficos:")
        print("1. - Gráfico de Barras")
        print("2. - Gráfico de Linhas")
        print("3. - Gráfico de Pizza")
        print("4. Sair")
        escolha = input("Escolha o tipo de gráfico (1-4): ").strip()

        if escolha == "1":
            # Gráfico de barras
            coluna = input("Informe a coluna para o eixo X: ").strip()
            if coluna in dados.columns:
                # Conta os valores únicos da coluna e plota como barras
                dados[coluna].value_counts().plot(kind='bar', title=f"Gráfico de Barras: {coluna}")
                plt.show()
            else:
                print("Coluna não encontrada!") # Mensagem de erro se a coluna não existir
        elif escolha == "2":
            # Gráficos de linhas
            coluna = input("Informe a coluna numérica para o gráfico de linhas: ").strip()
            if coluna in dados.columns:
                # Plota os valores da coluna como uma linha
                dados[coluna].plot(kind='line', title=f"Gráfico de Linhas: {coluna}")
                plt.show()
            else:
                print("Coluna não encontrada!")# Mensagem de erro se a coluna não existir
        elif escolha == "3":
            # Gráfico de pizza
            coluna = input("Informe a coluna categórica para o gráfico de pizza: ").strip()
            if coluna in dados.columns:
                # Conta os valores únicos e plota como gráfico de pizza
                dados[coluna].value_counts().plot(kind='pie',autopct='%1.1f%%',title=f"Gráfico de Pizza: {coluna}")
                plt.show()
            else:
                print("Coluna não encontrada!") # Mensagem de erro se a coluna não existir
        elif escolha == "4":
            # Sai do loop e encerra o menu de gráficos
            break
        else:
            print("Opção inválida. Tente novamente.") # Mensagem de erro para entradas inválidas
def exportar_resumo(estatisticas):
    # Exporta o resumo das estatísticas descritivas para um arquivo Excel.
    while True:
        # Pergunta ao usuário se deseja exportar o resumo
        escoha = input("Deseja exportar o resumo para um arquivo Excel? (s/n): ").strip().lower()
        if escolha == 's':
            # Solicita o caminho do arquivo para salvar
            caminho = input("Informe o caminho para salvar o arquivo (ex.: resumo.xlsx): ").strip()
            try:
                # Salva as estatísticas em forma Excel
                estatisticas.to_excel(caminho)
                print("Resumo exportado com sucesso!") # Confirmação de sucesso
                break
            except Exception as e:
                # Mensagem de erro se ocorrer algum problemas ao salvar
                print(f"Erro ao salvar o arquivo: {e}")
        elif escolha == 'n':
            # Sai do loop se o usuário não quiser exportar
            break
        else:
            print("Resposta inválida. Tente novamente.") # Mensagem para entradas inválidas

def main():
    # Função principal que organiza o fluxo do sistema de análise de dados.
    print("¨¨¨¨¨ Bem-vindo ao Sistema de Análise de Dados¨¨¨¨¨¨¨¨")
    # Passo 1: Carregar os dados
    dados = carregar_arquivo()
    # Passo 2: Validar os dados carregados
    validar_dados(dados)
    # Passo 3: Calcular estatísticas descritivas
    estatisticas = calcular_estatisticas(dados)
    # Passo 4: Gerar gráficos com base nos dados
    gerar_graficos(dados)
    # Passo 5: Exportar resumo das estatíticas, se desejado
    exportar_resumo(estatisticas)
    print("\nAnálise concluída. Obrigado por usar o sistema!") # Mensagem de encerramento

if __name__ == "__main__":
    main() # Chama a função principal para iniciar o programa