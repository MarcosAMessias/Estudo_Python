from PIL import Image # Biblioteca para manipulação de imagens
import os # Para limpar o terminal entre os frames da animação
import time # Para controlar o tempo entre os frames

# Mapeamento de tons de cinza para caracteres ASCII 
ASCII_CHARS = "@%#*+=:." # Caracteres em ordem de densidade visual (escuro -> claro)

def redimensionar_imagem(imagem, nova_largura=100):
    """
    Redimensiona a imagem mantendo a proporção.
    """
    largura, altura = imagem.size # Obtém as dimensões originais1
    proporcao = altura /largura / 1.65 # ajusta a proporção para compensar a largura dos caracteres
    nova_altura = int(nova_largura * proporcao) # Calcula a nova altura proporcional
    return imagem.resize((nova_largura, nova_altura)) # Redimensiona a imagem

def converter_para_cinza(imagem):
    """
    Converte a image para tons de cinza.
    """
    return imagem.convert("L") # 'L' indica tons de cinza

def mapear_pixels_para_ascii(imagem):
    """
    Mapeia cada pixel da imagem para um caractere ASCII com base na intensidade do tom de cinza 
    """
    pixels = imagem.getdata() # Obtém os valores dos pixels da imagem
    caracteres = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels]) # Mapeia para caracteres
    return caracteres

def gerar_arte_ascii(caminho_imagem, largura=100):
    """
    Converte uma imagem para a arte ASCII.
    """
    try:
        imagem = Image.open(caminho_imagem) # Abre a imagem
    except Exception as e:
        print(f"Erro ao abrir a imagem: {e}")
        return None
    
    # Redimensiona e converte para tons de cinza
    imagem = redimensionar_imagem(imagem, largura)
    imagem = converter_para_cinza(imagem)

    # Mapeia os pixels para caracteres ASCII
    caracteres_ascii = mapear_pixels_para_ascii(imagem)
    largura_imagem = imagem.width
    arte_ascii = "\n".join([caracteres_ascii[i:i+largura_imagem] for i in range (0, len(caracteres_ascii), largura_imagem)])
    return arte_ascii

def animar_arte_ascii(arte_ascii, repeticoes=10, intervalo=0.1):
    """
    Exibe a arte ASCII com animação no terminal.
    """
    linhas = arte_ascii.splitlines() # Divide a arte em linhas
    for _ in range(repeticoes): # Controla o número de repetições 
        for deslocamento in range(len(linhas)): # Controla o deslocamento vertical
            os.system("cls" if os.name == "nt" else "clear") # Limpa o terminal
            # Exibe as linhas deslocadas para criar o efeito de animação
            print("\n".join(linhas[deslocamento:] + linhas[:deslocamento]))
            time.sleep(intervalo) # Aguarda um curto período para o próximo frame

def main():
    """
    Função principal para executar o programa.
    """
    print("**** Gerador de Arte ASCII Animada ****")
    caminho_imagem = input("Digite o caminho da imagem (exemplo: 'imagem.jpg): ").strip()

    # Gera a arte ASCII
    arte_ascii = gerar_arte_ascii(caminho_imagem)
    if arte_ascii:
        print("\nArte gerada com sucesso!")
        print("Exibindo animação...")
        animar_arte_ascii(arte_ascii)
    else:
        print("Falha ao gerar a arte ASCII.")

if __name__ == "__main__":
    main()