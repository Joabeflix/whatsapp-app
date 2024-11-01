import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.style import Style
from PIL import Image, ImageTk
import pywhatkit as kit
import datetime

class MensagemWhatsAppApp:
    def __init__(self):
        self.tela = tk.Tk()
        self.setup_ui()
        
    def enviar_mensagem(self, mensagem, numero_telefone, hora, minuto):
        numero_usar = f'+55{numero_telefone}'
        kit.sendwhatmsg(numero_usar, mensagem, hora, minuto)

    def definir_minutos(self, minutos):
        hora_atual = datetime.datetime.now()
        nova_hora = hora_atual.hour
        novo_minuto = hora_atual.minute + minutos
        
        if novo_minuto >= 60:
            nova_hora += novo_minuto // 60
            novo_minuto %= 60
        
        if nova_hora > 23:
            nova_hora %= 24
        
        return nova_hora, novo_minuto

    def app_logic(self):
        numero = self.numero_de_telefone.get()
        minuto_usuario = self.tempo_minutos.get()
        minuto_usuario = 1 if minuto_usuario == '' else int(minuto_usuario)

        mensagem = self.caixa_de_mensagem.get("1.0", tk.END)
        hora, minuto = self.definir_minutos(minuto_usuario)
        print(mensagem)
        
        if len(numero) == 11:
            self.enviar_mensagem(mensagem=mensagem, numero_telefone=numero, hora=hora, minuto=minuto)
        else:
            messagebox.showinfo(title='Erro', message='Você não digitou um número válido', icon='error')

    def setup_ui(self):
        logo_tk = ImageTk.PhotoImage(file='logo.png')
        self.tela.iconphoto(False, logo_tk)

        tk.Label(self.tela, text="Número de telefone:").place(x=8, y=0)
        self.numero_de_telefone = tk.Entry(self.tela, width=30)
        self.numero_de_telefone.place(x=8, y=20)

        tk.Label(self.tela, text="Tempo (minutos)").place(x=200, y=0)
        self.tempo_minutos = tk.Entry(self.tela, width=8)
        self.tempo_minutos.place(x=218, y=20)

        tk.Label(self.tela, text="Descreva a mensagem abaixo:").place(x=8, y=45)
        self.caixa_de_mensagem = tk.Text(self.tela, width=35, height=6)
        self.caixa_de_mensagem.place(x=8, y=65)

        botao_iniciar = ttk.Button(self.tela, text='Programar Mensagem', command=self.app_logic, bootstyle='SUCCESS')
        botao_iniciar.place(x=90, y=186)

        self.tela.title('Mensagem Prog')
        self.tela.geometry('320x225')
        self.tela.mainloop()

if __name__ == "__main__":
    app = MensagemWhatsAppApp()
