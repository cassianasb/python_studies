name = input("Digite o nome: ")
age = int(input("Digite a idade: "))
contagiousDisease = input("Suspeita de doença infecto-contagiosa? ").upper()

if age >= 65:
    print("Paciente " + name + " COM prioridade.")
    if "SIM"==contagiousDisease:
        print("Encaminhe para sala AMARELA.")
    elif "NAO"==contagiousDisease:
        print("Encaminhe para sala BRANCA.")
    else:
        print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO.")
else:
    print("Paciente " + name + " SEM prioridade.")
    if "SIM"==contagiousDisease:
        print("Encaminhe para sala AMARELA.")
    elif "NAO"==contagiousDisease:
        print("Encaminhe para sala BRANCA.")
    else:
        print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO.")