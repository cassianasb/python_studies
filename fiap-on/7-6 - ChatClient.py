from socket import *

server = "127.0.0.1"
port = 43210

while True:
    obj_socket = socket(AF_INET, SOCK_STREAM)
    obj_socket.connect((server, port))
    msg = bytes(input("Sua mensagem: "), 'utf-8')
    obj_socket.send(msg)
    answer = obj_socket.recv(1024)
    print("Resposta do Servidor: ", str(answer)[2:-1])
obj_socket.close()