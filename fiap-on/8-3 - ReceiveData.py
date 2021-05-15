import serial
connection = ""
for port in range(10):
    try:
        connection = serial.Serial("COM"+str(port), 115200)
        print("Conectado na porta: ", connection.portstr)
        break
    except serial.SerialException:
        pass
if connection != "":
    while True:
        answer = connection.read()
        if answer == b'1':
            print("LED Ligado")
        else:
            print("LED Desligado")
    connection.close()
    print("Conexão encerrada")
else:
    print("Sem portas disponíveis")