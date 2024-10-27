import datetime

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


valor_hora, valor_minuto = definir_minutos(10)

