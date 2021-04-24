equipaments = []
values = []
serials = []
departaments = []
answer = "S"

while "S" == answer:
    equipaments.append(input("Equipamento: "))
    values.append(float(input("Valor: ")))
    serials.append(int(input("Serial: ")))
    departaments.append(input("Departamento: "))
    answer = input("Digite 'S' para continuar: ").upper()

descart = int(input("Digite o serial equipamento a ser descartado: "))
for index in range(0, len(equipaments)):
    if descart == serials[index]:
        del equipaments[index]
        del values[index]
        del serials[index]
        del departaments[index]
        break