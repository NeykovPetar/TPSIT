from email import message
from socket import AF_INET, SO_BROADCAST, SOCK_DGRAM, socket
from ssl import SOL_SOCKET  
from packet import Packet

BUFFER_SIZE = 1024
PORT = int(input("Inserire una porta: "))
HOST = "0.0.0.0"

exit = False

def chatserver(HOST,PORT):
    with  socket(AF_INET, SOCK_DGRAM) as s:  
        s.bind((HOST, PORT))  
        while exit == False:
            
            msg = s.recvfrom(BUFFER_SIZE)
            print(msg)
            pkt=Packet.from_bytes(msg[0])
            print(pkt.username + " ha inviato il messaggio: " + pkt.message + ".")

if __name__ == "__main__":
    chatserver(HOST,PORT)