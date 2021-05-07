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

deprecieted = input("Digite oequipamento a ser depreciado: ")
for index in range(0, len(equipaments)):
    if deprecieted == equipaments[index].upper:
        new_value = values[index] * 0.9
        values[index] = new_value