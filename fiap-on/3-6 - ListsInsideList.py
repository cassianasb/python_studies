inventory = []
answer = "S"
while "S" == answer:
    equipament = [input("Equipamento: "), float(input("Valor: ")), int(input("Serial: ")), input("Departamento: ")]
    inventory.append(equipament)
    answer = input("Digite 'S' para continuar: ").upper()

for element in inventory:
    print("Nome.........:", element[0])
    print("Valor........:", element[1])
    print("Serial.......:", element[2])
    print("Departamento.:", element[3])

search = input("Digite o nome do equipamento que deseja buscar: ")
for element in inventory:
    if element[0] == search:
        print("Valor........:", element[1])
        print("Serial.......:", element[2])
        print("Departamento.:", element[3])

deprecieted = input("Digite o nome do equipamento a ser depreciado: ")
for element in inventory:
    if element[0] == deprecieted:
        print("Valor antigo: ", element[1])
        element[1] = element[1] * 0.9
        print("Valor novo: ", element[1])

descart = int(input("Digite o serial equipamento a ser descartado: "))
for element in inventory:
    if element[2] == descart:
        inventory.remove(element)

for element in inventory:
    print("Nome.........:", element[0])
    print("Valor........:", element[1])
    print("Serial.......:", element[2])
    print("Departamento.:", element[3])

values = []
for element in inventory:
  values.append(element[1])
if len(values)>0:
  print("O equipamento mais caro custa: ", max(values))
  print("O equipamento mais barato custa: ", min(values))
  print("O total de equipamentos é de: ", sum(values))