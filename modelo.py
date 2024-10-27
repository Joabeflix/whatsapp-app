import pywhatkit as kit

# Número de telefone no formato internacional com o código do país.
numero_telefone = "+5511999999999"

# Mensagem a ser enviada
mensagem = "Olá! Esta é uma mensagem enviada automaticamente pelo Python."

# Horário em que a mensagem será enviada (formato 24 horas)
hora = 14
minuto = 30

# Envia a mensagem
kit.sendwhatmsg(numero_telefone, mensagem, hora, minuto)
