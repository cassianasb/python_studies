users={}
users={
    "Chaves":["Chaves Silva","17/06/2017","Recep_01"],
    "Quico":["Enrico Flores","03/06/2017","Raiox_02"]
}
# Add item
users["Florinda"] = ["Florinda Flores", "26/11/2017", "Recep_01"]
# Update item
users["Florinda"] = ["Florinda Flores", "26/11/2018", "Recep_01"]
print(users)

print("##############========#########")
print("Dados: ", users.get("Chaves"))