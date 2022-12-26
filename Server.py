import socket
import sys
import threading
from Log import Logs
from datetime import datetime

HOST = '0.0.0.0'
PORT = 9999

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST, PORT))
socket.listen(10)
print("Servidor rodando em: " + HOST + ":" + str(PORT))


def fileSend():
    data = datetime.today().strftime('%d/%m/%Y')
    hora = datetime.today().strftime('%Hh%M')
    while 1:
        conn, addr = socket.accept()
        print("[*] Conexao aceita de: ", addr[0], ":", addr[1])
        reqFile = conn.recv(9999)
        try:
            with  open(reqFile, 'rb') as file_to_send:
                for data in file_to_send:
                    conn.sendall(data)
                log = Logs(str(data)+" "+str(hora)+" "+str(addr[0])+" "+str(addr[1])+": "+str(reqFile))
                log.saveLog()
            conn.close()
        except:
            print("Houve um erro")
            log = Logs(str(data) + " " + str(hora) + " " + str(addr[0]) + " " + str(addr[1]) + ": erro: " + str(sys.exc_info()[0]))
            log.saveLog()
            conn.close()

    socket.close()
while True:
    client_handler = threading.Thread(target=fileSend())
    client_handler.start()  # Inicia a thread
