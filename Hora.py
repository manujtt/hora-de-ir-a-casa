import time
hora = time.strftime("%H")
minutos = time.strftime("%M")

if int(hora)>=19:
    print("Es hora de ir a casa")
else:
    print("quedan {} horas y {} minutos para irnos a casa". format(18- int(hora), 59-int(minutos)))