import json
import os
inventory = {}
if os.path.exists("inventario_json.json"):
    with open("inventory.json", "r") as json_file:
        inventory = json.load(json_file)
option = int(input("Digite: \n<1> para registrar ativo \n<2> para exibir ativos armazenados: "))
while option > 0 and option < 3:
    if option == 1:
        answer = "S"
        while answer == "S":
            inventory[input("Digite o número patrimonial: ")] = [
                input("Digite a data da última atualização: "),
                input("Digite a descrição: "),
                input("Digite o departamento: ")]
            answer = input("Digite <S> para continuar. ").upper()
        with open("inventory.json", "w") as json_file:
            json.dump(inventory, json_file)
        print("JSON gerado!!!!")
    elif option==2:
        with open("inventory.json", "r") as json_file:
            result = json.load(json_file)
            for key, data in result.items():
                print("Data.........: ", data[0])
                print("Descrição....: ", data[1])
                print("Departamento.: ", data[2])
    option = int(input("Digite: \n<1> para registrar ativo \n<2> para exibir ativos armazenados: "))