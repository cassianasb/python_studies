users = {}
answer = "S"
emails = []
while "S" == answer:
    emails.append(input("Digite um e-mail: ").lower())
    answer = input("Digite <S> para continuar: ").upper()

tuplee = list(enumerate(emails))
for key in range(0,len(tuplee)):
    print("Email: ", tuplee[key][1])
    users[tuplee[key]]=[input("Digite o nome: "), input("Digite o nível: ")]

for key, date in users.items():
    print("Usuario.: ", key[0])
    print("Email...: ",key[1])
    print("Nome....: ", date[0])
    print("Nível...: ", date[1])