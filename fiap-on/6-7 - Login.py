import getpass

user = input("Digite o usuário: ").upper()
password = getpass.getpass("Digite a senha: ")

if user == "USERADM" and password == "OutTime":
    print("Usuário logado")
else:
    print("Login Negado")