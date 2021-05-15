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
        answer = connection.readline()
        print(answer.decode())
    connection.close()
    print("Conexão encerrada")
else:
    print("Sem portas disponíveis")