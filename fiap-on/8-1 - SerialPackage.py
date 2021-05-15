import serial
connection = ""
for port in range(10):
    try:
        connection = serial.Serial("COM"+str(port), 115200, timeout=0.5)
        print("Conectado na porta: ", connection.portstr)
        break
    except serial.SerialException:
        pass
if connection != "":
    connection.close()
    print("Conexão encerrada")
else:
    print("Sem portas disponíveis")