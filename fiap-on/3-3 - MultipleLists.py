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

for index in range(0, len(equipaments)):
    print("Equipamento: ", (index + 1))    
    print("Nome: ", equipaments[index])
    print("Valor: ", values[index])
    print("Serial: ", serials[index])
    print("Departamento: ", departaments[index])

search = input("Digite o nome do equipamento que deseja buscar: ")
for index in range(0, len(equipaments)):
    if equipaments[index] == search:
        print("Valor: ", values[index])
        print("Serial: ", serials[index])
        print("Departamento: ", departaments[index])
