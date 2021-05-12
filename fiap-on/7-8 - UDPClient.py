from socket import *

server = "127.0.0.1"
port = 43210
obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.connect((server, port))
out = ""
while out != "X":
    msg = input("Sua mensagem: ")
    obj_socket.sendto(msg.encode(), (server, port))
    datas, origem = obj_socket.recvfrom(65535)
    print("Resposta do Servidor: ", datas.decode())
    out = input("Digite <X> para sair: ").upper()
obj_socket.close()