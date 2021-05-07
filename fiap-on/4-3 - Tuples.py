ips = {}
answer = "S"
while "S" == answer:
    ips[(input("Digite os dois primeiros octetos: "),
       input("Digite os dois últimos octetos: "))] = input("Nome da máquina: ")
    answer = input("Digite <S> para continuar: ").upper()

print(ips)

print("Exibindo ip´s: ")
for ip in ips.keys():
    print(ip[0]+"."+ip[1])

print("Exibindo máquinas com o mesmo endereço: ")
search = input("Digite os dois últimos octetos: ")
for ip, name in ips.items():
    print("Máquinas no mesmo endereço (redes diferentes)")
    if(ip[1] == search):
        print(name)

print("Exibindo as máquinas que compõem uma mesma rede: ")
net = input("Digite os dois primeiros octetos: ")
for ip, name in ips.items():
    if(ip[0] == net):
        print(name)