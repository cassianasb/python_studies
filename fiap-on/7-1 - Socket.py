import socket
answer = "S"
while(answer == "S"):
    url = input("Digite uma url: ")
    ip = socket.gethostbyname(url)
    print("O IP referente à url informada é: ", ip)
    answer = input("Digite <s> para continuar: ").upper()