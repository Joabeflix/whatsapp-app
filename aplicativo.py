import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import *
from ttkbootstrap.style import Style
from PIL import Image, ImageTk
import pywhatkit as kit
from datetime import datetime

tela = tk.Tk()
tela.title('Mensagem Prog')
tela.geometry('300x400')
logo_tk = ImageTk.PhotoImage(file='logo.png')
tela.iconphoto(False, logo_tk)
##################################################################
# numero_telefone = "+5511999999999"
def enviar_mensagem(mensagem, numero_telefone, hora, minuto):

    kit.sendwhatmsg(mensagem, numero_telefone, hora, minuto)
    return 0

def app():
    """
    horas_minutos = datetime.now().strftime("%H:%M:%S")
    hora_atual = horas_minutos[:2]
    minuto_atual = horas_minutos[3:5]
    """
    mensagem = entrada_mensagem.get()
    numero_telefone = entrada_numero_telefone.get()
    qtd_minutos = entrada_qtd_minutos.get()

def escrever_mensagem():
    tela_mensagem = tk.Tk()
    tela_mensagem.title('Mensagem')
    tela_mensagem.geometry('360x85')

    def enviar_mensagem():
        mensagem = entrada_mensagem.get()
        
        return mensagem
    
    entrada_mensagem = tk.Entry(tela_mensagem, width=30)
    entrada_mensagem.place(x=10, y=10)
    tela_mensagem.mainloop()

    return  entrada_mensagem

escrever_mensagem = tk.Button(tela, text='Escrever mensagem', command=escrever_mensagem)
escrever_mensagem.place(x=95, y=30)


tela.mainloop()
