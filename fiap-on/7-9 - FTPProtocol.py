from ftplib import *

active_ftp = False
ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())

user = input("Digite o usuário: ")
password = input("Digite a senha: ")
ftp.login(user, password)
print("Diretório atual de trabalho: ", ftp.pwd())

ftp.cwd("pub")
print("Diretório atual: ", ftp.pwd())

#print(ftp.retrlines("LIST"))
print(ftp.dir())

ftp.quit()