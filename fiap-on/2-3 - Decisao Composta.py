name = input("Digite o nome: ")
age = int(input("Digite a idade: "))
contagiousDisease = input("Suspeita de doença infecto-contagiosa? ").upper()

if age >= 65 and "SIM"==contagiousDisease:
    print("O paciente " + name + " será direcionado para sala AMARELA - COM prioridade.")
elif age < 65 and "SIM"==contagiousDisease:
    print("O paciente " + name + " será direcionado para sala AMARELA - SEM prioridade.")
elif age >= 65 and "NAO"==contagiousDisease:
    print("O paciente " + name + " será direcionado para sala BRANCA - COM prioridade.")
elif age < 65 and "NAO"==contagiousDisease:
    print("O paciente " + name + " será direcionado para sala BRANCA - SEM prioridade.")
else:
    print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO.")