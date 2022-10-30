from logging import exception
from socket import AF_INET, SOCK_DGRAM, socket, timeout

def chatServer():
      
    with socket(AF_INET, SOCK_DGRAM) as s:                  #inizializziamo il socket
        host ="0.0.0.0"
        porta = 7777
        s.bind((host,porta))                                #eseguaiamo il bind della porta
        indirizzo = (host,porta)                            #tupla con host e porta
        buffer = 8192
        
        dati,indirizzo = s.recvfrom(buffer)                 #leggiamo la prima parte dei dati dal buffer (indirizzo e porta)
        print ("File ricevuto:",dati.strip())               #la funzione strip serve per rimuovere gli spazi all'inzio e alla fine della stringa
        f = open(dati.strip(),'wb')                         #apriamo i dati in modalità wb (scrittura binaria)
        dati,indirizzo = s.recvfrom(buffer)                 #leggiamo la seconda parte dei dati dal buffer (dati)

        try:
            while(dati):
                f.write(dati)                               #scriviamo i dati
                s.settimeout(1)                             #impostiamo un timeout di un secondo
                dati,indirizzo = s.recvfrom(buffer)         
        except timeout:                                     #dopo il timeout...
            f.close()
            print("File trasferito con successo!")

if __name__ == "__main__":
    chatServer()