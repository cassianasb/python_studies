from functions.Functions import *

inventory=[]
print("Preenchendo")
add_items(inventory)
print("Exibindo")
print_list(inventory)

print("Pesquisando")
search_items(inventory)
print("Alterando")
down_value_items(inventory, 20)

print("Excluindo")
print(descart_items(inventory))
print_list(inventory)

print("Resumindo")
values_resume(inventory)