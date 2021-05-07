def add_items(listt):
    answer = "S"
    while "S" == answer:
        equipament = [input("Equipamento: "), float(input("Valor: ")), int(input("Serial: ")), input("Departamento: ")]
        listt.append(equipament)
        answer = input("Digite 'S' para continuar: ").upper()

def print_list(listt):
    for element in listt:
        print("Nome.........:", element[0])
        print("Valor........:", element[1])
        print("Serial.......:", element[2])
        print("Departamento.:", element[3])

def search_items(listt):
    search = input("Digite o nome do equipamento que deseja buscar: ")
    for element in listt:
        if element[0] == search:
            print("Valor........:", element[1])
            print("Serial.......:", element[2])
            print("Departamento.:", element[3])

def down_value_items(listt):
    deprecieted = input("Digite o nome do equipamento a ser depreciado: ")
    for element in listt:
        if element[0] == deprecieted:
            print("Valor antigo: ", element[1])
            element[1] = element[1] * 0.9
            print("Valor novo: ", element[1])

def descart_items(listt):
    descart = int(input("Digite o serial equipamento a ser descartado: "))
    for element in listt:
        if element[2] == descart:
            listt.remove(element)

def values_resume(listt):
    values = []
    for element in listt:
        values.append(element[1])
    if len(values)>0:
        print("O equipamento mais caro custa: ", max(values))
        print("O equipamento mais barato custa: ", min(values))
        print("O total de equipamentos é de: ", sum(values))

def call_menu():
    option = int(input("Digite: \n<1> para registrar ativo \n<2> para persistir em arquivo \n<3> para exibir ativos armazenados: "))
    return option

def register(dic):
    answer="S"
    while answer=="S":
        dic[input("Digite o número patrimonial: ")]=[
        input("Digite a data da última atualização: "),
        input("Digite a descrição: "),
        input("Digite o departamento: ")]
        answer=input("Digite <S> para continuar. ").upper()

def persist(dic):
    with open("invetory.csv", "a") as inv:
        for key, value in dic.items():
            inv.write(key + ";" + value[0] + ";" + value[1] + ";" +value[2] + "\n")
    return "Persistido com sucesso"

def show():
    with open("invetory.csv", "r") as inv:
        lines=inv.readlines()
    return lines