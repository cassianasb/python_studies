import os
from ftplib import *

def writeLine(data):
    fil.write(data)
    fil.write(os.linesep)

active_ftp = False
ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())
ftp.login()

file = 'LEIAME'
ftp.set_pasv(active_ftp)
with open (file, 'w') as fil:
    ftp.retrlines('RETR README', writeLine)
ftp.quit()