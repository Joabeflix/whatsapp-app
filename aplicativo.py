import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap import *
from ttkbootstrap.style import Style
from PIL import Image, ImageTk
import pywhatkit as kit
import datetime

# mostrar mensagem = messagebox.showinfo('Mensagem!')

def enviar_mensagem(mensagem, numero_telefone, hora, minuto):
    numero_usar = f'+55{numero_telefone}'
    kit.sendwhatmsg(numero_usar, mensagem, hora, minuto)
    return 0

def definir_minutos(minutos):
    hora_atual = datetime.datetime.now()

    nova_hora = hora_atual.hour
    novo_minuto = hora_atual.minute + minutos
    
    if novo_minuto >= 60:
        nova_hora += novo_minuto // 60
        novo_minuto = novo_minuto % 60
    
    if nova_hora > 23:
        nova_hora = nova_hora % 24
    
    return nova_hora, novo_minuto


def app():
    numero = numero_de_telefone.get()

    minuto_usuario = tempo_minutos.get()
    if minuto_usuario == '':
        minuto_usuario = 1

    mensagem = caixa_de_mensagem.get("1.0", tk.END)
    hora, minuto = definir_minutos(int(minuto_usuario))
    print(mensagem)
    
    if len(numero) == 11:
        enviar_mensagem(mensagem=mensagem, numero_telefone=numero, hora=hora, minuto=minuto)
    else:
        messagebox.showinfo(title='Erro', message='Você não digitou um número válido', icon='error')

tela = tk.Tk()
"""
def funcao_numeros_recentes():
    lista = []
    with open('numeros_recentes.txt') as arquivos:
        for linha in arquivos:
            lista.append(linha.strip())
            print(linha.strip())
    return lista

contatos_recentes = funcao_numeros_recentes()
var_selecao = StringVar(value="Selecione")
"""
logo_tk = ImageTk.PhotoImage(file='logo.png')
tela.iconphoto(False, logo_tk)

tk.Label(tela, text="Número de telefone:").place(x=8, y=0)
numero_de_telefone = tk.Entry(tela, width=30)
numero_de_telefone.place(x=8, y=20)


tk.Label(tela, text="Tempo (minutos)").place(x=200, y=0)
tempo_minutos = tk.Entry(tela, width=8)
tempo_minutos.place(x=218, y=20)


tk.Label(tela, text="Descreva a mensagem abaixo:").place(x=8, y=45)
caixa_de_mensagem = tk.Text(tela, width=35, height=6)
caixa_de_mensagem.place(x=8, y=65)

botao_iniciar = ttk.Button(tela, text='Programar Mensagem', command=app, bootstyle=SUCCESS)
botao_iniciar.place(x=90, y=186)
botao_iniciar.configure()

tela.title('Mensagem Prog')
tela.geometry('320x225')
tela.mainloop()
