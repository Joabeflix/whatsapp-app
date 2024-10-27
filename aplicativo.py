import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import *
from ttkbootstrap.style import Style
from PIL import Image, ImageTk
import pywhatkit as kit
from datetime import datetime

tela = tk.Tk()

def funcao_numeros_recentes():
    lista = []
    with open('contatos_recentes.txt') as arquivos:
        for linha in arquivos:
            lista.append(linha.strip())
            print(linha.strip())
    return lista




logo_tk = ImageTk.PhotoImage(file='logo.png')
tela.iconphoto(False, logo_tk)

def enviar_mensagem(mensagem, numero_telefone, hora, minuto):

    kit.sendwhatmsg(mensagem, numero_telefone, hora, minuto)
    return 0





botao_iniciar = tk.Button(tela, text='Programar Mensagem')
botao_iniciar.place(x=90, y=360)

numero_de_telefone = tk.Entry(tela, width=30)
numero_de_telefone.place(x=8, y=10)

caixa_de_mensagem = tk.Text(tela, width=35, height=6)
caixa_de_mensagem.place(x=8, y=55)








tela.title('Mensagem Prog')
tela.geometry('300x400')
tela.mainloop()
