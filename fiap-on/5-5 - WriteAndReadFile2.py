from functions.Functions import *
inventory={}
option=call_menu()
while option>0 and option<4:
    if option==1:
        register(inventory)
    elif option==2:
        persist(inventory)
    elif option==3:
        result = show()
        for line in result:
            print("Equipamento: ", line[line.find(";")+1:-1])
            infos = line.split(";")
            print("Data.........: ", infos[1])
            print("Descrição....: ", infos[2])
            print("Deapartamento: ", infos[3])
    option = call_menu()