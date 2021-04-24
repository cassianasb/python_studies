name = input("Digite o nome: ")
age = int(input("Digite a idade: "))
priority = "NÃO"
if age > 65:
    priority = "SIM"
print("O paciente " + name + " possui atendimento prioritário? " + priority)