import os
from ftplib import *

active_ftp = False
ftp = FTP(input("Digite o FTP que se deseja conectar: "))
print(ftp.getwelcome())
user = input("Digite o usuario: ")
password = input("Digite a senha: ")
ftp.login(user, password)
print("Conexão bem sucedida. \nDiretório atual de trabalho: ", ftp.pwd()," ")

menu="1"
while menu == "1" or menu == "2" or menu == "3":
    menu=input("Escolha a opção desejada: \n<1> - para Listar arquivos \n<2> - para definir um diretório \n<3> - para baixar um arquivo: ")
    if menu=="1":
        print(ftp.dir())
    elif menu=="2":
        ftp.cwd(input("Digite o diretório que deseja entrar: "))
        print("\nDiretório corrente é: ", ftp.pwd())
    elif menu=="3":
        type = input("Digite <B> para arquivo binário ou \n qualquer outra letra para arquivo ASCII: ").upper()
        if type=="B":
            with open(input("Digite o nome do arquivo destino: "), 'wb') as file:
                ftp.retrbinary('RETR ' + input("Arquivo de origem: "), file.write)
        else:
            with open(input("Digite o nome do arquivo destino: "), 'w') as file:
                def escreverLinha(data):
                    file.write(data)
                    file.write(os.linesep)
                ftp.retrlines('RETR ' + input("Arquivo de origem:"), escreverLinha)
        print("Arquivo baixado com sucesso!\n")
ftp.quit()