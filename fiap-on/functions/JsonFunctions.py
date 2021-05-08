import json
import os
def call_menu():
    option = int(input("Digite: \n<1> para registrar ativo \n<2> para exibir ativos armazenados: "))
    return option

def read_file(file):
    if os.path.exists(file):
        with open(file, "r") as json_file:
            dictonary=json.load(json_file)
    else:
        dictonary = {}
    return dictonary

def save_file(dictonary, file):
    with open(file, "w") as json_file:
        json.dump(dictonary, json_file)

def register(dictonary, file):
    answer = "S"
    while answer == "S":
        dictonary[input("Digite o número patrimonial: ")] = [
            input("Digite a data da última atualização: "),
            input("Digite a descrição: "), input("Digite o departamento: ")]
        answer = input("Digite <S> para continuar.").upper()
        save_file(dictonary, file)
    return "JSON gerado!!!!"

def show(file):
    dictonary = read_file(file)
    for key, data in dictonary.items():
        print("Data.........: ", data[0])
        print("Descrição....: ", data[1])
        print("Departamento.: ", data[2])