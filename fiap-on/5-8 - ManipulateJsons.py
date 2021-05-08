from functions.JsonFunctions import *

inventory = read_file("inventory.json")
option = call_menu()
while option > 0 and option < 3:
    if option == 1:
        print(register(inventory, "inventory.json"))
    elif option == 2:
        show("inventory.json")
    option = call_menu()