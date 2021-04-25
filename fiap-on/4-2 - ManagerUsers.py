def question():
    option = input("O que deseja realizar?\n <I> - Para Inserir um usuário \n <P> - Para Pesquisar um usuário \n <E> - Para Excluir um usuário \n <L> - Para Listar um usuário: ").upper()
    return option

def insert(dictonary):
    key = input("Digite o login: ")
    dictonary[key]=[input("Digite o nome: "), input("Digite a última data de acesso: "), input("Qual a última estação acessada: ")]

def search(dictonary, key):
    datas = dictonary.get(key)
    if datas != None:
        print("Nome...........: " + datas[0])
        print("Último acesso..: " + datas[1])
        print("Última estação.: " + datas[2])

def delete(dictonary, key):
    if dictonary.get(key) != None:
        del dictonary[key]
        print("Objeto Eliminado")

def printUsers(dictonary):
    for key, value in dictonary.items():
        print("Objeto......")
        print("Login: ", key)
        print("Dados: ", value)

users = {}
option = question()
while "I" == option or "P" == option or "E" == option or "L" == option:
    if "I" == option:
        insert(users)
    elif "P" == option:
        search(users, input("Digite o login do usuário que deseja pesquisar: "))
    elif "E" == option:
        delete(users, input("Digite o login do usuário que deseja deletar: "))
    elif "L" == option:
        printUsers(users)
    option = question()