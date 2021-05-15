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
    action = input("Digite:\n <L> para Ligar\n <D> para Desligar: ").upper()
    while action == "L" or action == "D":
        if action == "L":
            connection.write(b'1')
        else:
            connection.write(b'0')
        action = input("Digite:\n <L> para Ligar\n <D> para Desligar: ").upper()
    connection.close()
    print("Conexao encerrada")
else:
    print("Sem portas disponíveis")