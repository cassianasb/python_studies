import serial
import json
import time
from datetime import datetime
connection = ""
for port in range(10):
    try:
        connection = serial.Serial("COM"+str(port), 115200)
        print("Conectado na porta: ", connection.portstr)
        break
    except serial.SerialException:
        pass
if connection != "":
    dicionary = {}
    cont = 0
    while cont < 10:
        answer = connection.readline()
        dicionary[str(datetime.now())] = [answer.decode('utf-8')[0:3]]
        print(answer.decode('utf-8')[0:3])
        cont+=1
    with open('Temperature.json', "w") as file:
        json.dump(dictionary, file)
    connection.close()
    print("Conexão encerrada")
else:
    print("Sem portas disponíveis")