from datetime import datetime

hora_atual = datetime.now().strftime("%H:%M:%S")
print(hora_atual)
hora_atual2 = hora_atual[:2]
minuto = hora_atual[3:5]
print(hora_atual2)
print(minuto)
# Comentário de teste
