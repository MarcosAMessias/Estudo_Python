import tkinter as tk # Importa a biblioteca Tkinter para criar a interface gráfica

# Função que processa a mensagem digitada pelo usuário
def process_message():
    user_message = entry.get() # Obtém o texto digitado pelo usuário no campo de entrada
    if not user_message.strip(): # Verifica se a mensagem está vazia
        return # Se estiver vazia, a função é encerrada
    
    # Exibe a mensagem do usuário na área de histórico do chat
    chat_history.insert(tk.END, f"Você: {user_message}\n")

    # Converte a mensagem para letras minúsculas para facilitar a detecção de palavras-chaves
    user_message = user_message.lower()

    # Verifica palavras-chaves e define a resposta do chatbot
    if "dicas" in user_message:
        bot_response = "Aqui vão algumas dicas: \n- Evite shampoos com sulfato. \n- Use sempre leave-in para definição. "
    elif "cronograma capilar" in user_message:
        bot_response = "O cronograma capilar envolve hidratação, nutrição e reconstrução. Para mais dicas, diga 'hidratação' ou 'reconstrução'."
    elif "produtos" in user_message:
        bot_response = "Produtos recomendados: \n- Creme de pentear. \n- Gel ou gelatina. \n- Máscara de nutrição com óleos naturais."
    elif "receitas caseiras" in user_message:
        bot_response = "Receita com babosa: Extraia o gel da folha, misture com sua máscara favorita e aplique por 20 minutos."
    elif "frizz" in user_message:
        bot_response = "Para evitar frizz: \n- Use toalha de microfibra ou algodão. \n- Finalize com óleo para selar as pontas."
    elif "sair" in user_message:
        root.destroy() # Fecha a janela se o usuário digitar "sair"
        return
    else:
        # Resposta padrão para mensagens desconhecidas
        bot_response = "Desculpe, ainda não sei como responder a isso. Tente perguntar sobre 'dicas', 'produtos' ou 'cronograma capilar'."

    # Exibe a resposta do chatbot na área de histórico
    chat_history.insert(tk.END, f"CachoBot: {bot_response}\n")

    # Limpa o campo de entrada para que o usuário possa digitar uma nova mensagem
    entry.delete(0,tk.END)

# Cria a janela principal da interface gráfica
root = tk.Tk()
root.title("CachoBot - Assistente para Cabelos Cacheados") # Define o título da janela

# Adiciona um área para exibir as opções disponíveis
options_label = tk.Label(root, text="Pergunte sobre:\n- Dicas\n- Cronograma Capilar\n- Produtos\n- Receitas Caseiras\n- Frizz\nDigite 'sair' para encerrar.", justify="left")
options_label.pack(padx=10, pady=5) # Posiciona o rótulo na janela


# Adiciona uma área de texto para exibir o histórico do bate-papo
chat_history = tk.Text(root, height=20, width=50, state=tk.NORMAL)
chat_history.pack(padx=10, pady=5) # Posiciona a área de texto na janela

# Adiciona um campo de entrada para o usuário digitar mensagens
entry = tk.Entry(root, width=40)
entry.pack(padx=10, pady=5) # Posiciona o campo de entrada na janela

# Adiciona um botão para enviar mensagem
send_button = tk.Button(root, text="Enviar", command=process_message) # Associa o botão à função 'process_message'
send_button.pack(pady=5) # Posiciona o botão na janela

# Inicia o loop principal da interface gráfica (mantém a janela aberta e ativa)
root.mainloop()

