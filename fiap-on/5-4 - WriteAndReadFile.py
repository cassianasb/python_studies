inventory={}
option=int(input("Digite: \n<1> para registrar ativo \n<2> para persistir em arquivo \n<3> para exibir ativos armazenados: "))
while option>0 and option<4:
    if option==1:
        answer="S"
        while answer=="S":
            inventory[input("Digite o número patrimonial: ")]=[
            input("Digite a data da última atualização: "),
            input("Digite a descrição: "),
            input("Digite o departamento: ")]
            answer=input("Digite <S> para continuar.").upper()
    elif option==2:
        with open("inventory.csv", "a") as inv:
            for key, value in inventory.items():
                inv.write(key + ";" + value[0] + ";" + value[1] + ";" + value[2] + "\n")
                print("Persistido com sucesso!")
    elif option==3:
        with open("inventory.csv", "r") as inv:
            print(inv.readlines())
    option=int(input("Digite: \n<1> para registrar ativo \n<2> para persistir em arquivo \n<3> para exibir ativos armazenados: "))