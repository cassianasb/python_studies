from socket import *
server = "127.0.0.1"
port = 43210
obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.bind((server, port))
obj_socket.listen(2)
print("Aguardando cliente....")
while True:
    con, client = obj_socket.accept()
    print("Conectado com: ", client)
    while True:
        received = str(con.recv(1024))
        print("Recebemos: ", received)
        sended = b'Oi cliente'
        con.send(sended)
        break
    con.close()