from socket import *

server = "127.0.0.1"
port = 43210
obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.bind((server, port))
print("Servidor pronto....")
while True:
    datas, origem = obj_socket.recvfrom(65535)
    print("Origem..........: ", origem)
    print("Dados recebidos.: ", datas.decode())
    answer = input("Digite a resposta: ")
    obj_socket.sendto(answer.encode(), origem)
obj_socket.close()