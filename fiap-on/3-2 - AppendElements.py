list =[]
answer = "S"
while "S" == answer:
    listt.append(input("Equipamento: "))
    listt.append(float(input("Valor: ")))
    listt.append(int(input("Serial: ")))
    listt.append(input("Departamento: "))
    answer = input("Digite 'S' para continuar: ").upper()

for element in listt:
    print(element)