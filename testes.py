import pywhatkit as kit

def enviar_mensagem(mensagem, numero_telefone, hora, minuto):
    numero_usar = f'+55{numero_telefone}'
    kit.sendwhatmsg(numero_usar, mensagem, hora, minuto)


enviar_mensagem('teste', '27997255922', 21, 30)



