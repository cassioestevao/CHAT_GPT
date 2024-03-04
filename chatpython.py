import openai
import tkinter as tk
from tkinter import PhotoImage


openai.api_key = "chave api"


root = tk.Tk()
root.title("ChatAssist | Cássio Estevão")
root.config(bg="white")
root.resizable(False, False)


def enviar_mensagem(mensagem):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você está conversando com o chat GPT indiretamente!"},
            {"role": "user", "content": mensagem},
        ],
    )
    return response["choices"][0]["message"]["content"]

def enviar_mensagem_gui():
    mensagem = entry.get()
    response = enviar_mensagem(mensagem)
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, f"Você: {mensagem}\n")
    chat_history.insert(tk.END, f"Assistente: {response}\n\n")
    chat_history.config(state=tk.DISABLED)
    entry.delete(0, tk.END)

chat_history = tk.Text(root, 
                       height=20, 
                       width=70, 
                       state=tk.DISABLED
                       )
entry = tk.Entry(root, 
                 width=80
                 )
send_button = tk.Button(root, 
                        text="Enviar", 
                        command=enviar_mensagem_gui,
                        bg="white"
                        )

python_logo = PhotoImage(file="python_logo.png",height=50)
logo_label = tk.Label(root, image=python_logo)
logo_label.pack()

chat_history.pack()
entry.pack()
send_button.pack()

tk.mainloop()
