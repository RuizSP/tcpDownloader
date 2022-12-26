import socket
import os
import sys
from distlib.compat import raw_input

HOST = '0.0.0.0'
PORT = 9999
downloadDir = "arquivos"

filename = raw_input("Digite o nome do arquivo: ")
socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket1.connect((HOST, PORT))
socket1.send(bytes(filename, 'utf-8')) #converte a string filename para byte e envia para o socket do servidor

with open(os.path.join(downloadDir, filename), 'wb') as file_to_write:
    while True:
        data = socket1.recv(9999)
        if not data:
            break
        file_to_write.write(data)
        print("baixando arquivo")

    file_to_write.close()
print("arquivo Baixado com sucesso")
try:
    print("Corrigir")
except:
    print("houve um erro: " + str(sys.exc_info()[0]))

socket1.close()
