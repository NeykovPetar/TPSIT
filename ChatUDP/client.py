from socket import AF_INET, SOCK_DGRAM, socket
from server import PORT
from packet import Packet

utente = str(input("Inserire il nome utente: "))
adress = str(input("Inserire il tuo indirizzo: "))


def chatclient():
     
    with  socket(AF_INET, SOCK_DGRAM) as s:
        while True:
            msg = input("chat: ")
            messaggio = Packet(utente,msg)
            messaggio = messaggio.to_bytes()
            s.sendto(messaggio, (adress,PORT))
  
if __name__ == "__main__":
    chatclient()