name = input("Digite o nome do funcionário: ")
enterprise = input("Digite o nome da empresa: ")
employeesAmount = int(input("Digite a quantidade de funcionários: "))
monthlyPayment = float(input("Digite a média da mensalidade: "))

print(name + " trabalha na empresa " + enterprise)
print("Possui ", employeesAmount, " funcionários")
print("A média da mensalidade é " + str(monthlyPayment))

print("=============== Verifique os Tipos de Dados Abaixo: ===============")
print("O tipo de dado de [name] é: ", type(name))
print("O tipo de dado de [enterprise] é: ", type(enterprise))
print("O tipo de dado de [employeesAmount] é: ", type(employeesAmount))
print("O tipo de dado de [monthlyPayment] é: ", type(monthlyPayment))

responsible = input("Digite o nome do responsável: ")
employee = input("Digite o nome do funcionário: ")
event = input("Digite o nome do evento: ")
reimbursedAmount  = float(input("Digite ao valor a ser ressarcido: "))

print("Declaaro para o senhor " + responsible + " que o senhor " + employee + "s esteve presente no evento " + event + " e gastou o valor R$ " + str(reimbursedAmount) + " com a entrada.")