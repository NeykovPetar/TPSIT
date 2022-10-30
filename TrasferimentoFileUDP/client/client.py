from socket import AF_INET, SOCK_DGRAM, socket

def chatClient():
    
    with socket(AF_INET, SOCK_DGRAM) as s:                          #inzializziamo il socket
        host="127.0.0.1"
        porta = 7777
        buffer = 8192
        indirizzo = (host,porta)                                    #tupla con indirizzo e porta 

        try:                                                        #se il file viene trovato...
            nome_file = input(str("Inserisci il nome del file: "))
            f = open(nome_file.strip(),"rb")                        #apertura file in modalità rb (lettura binaria)
            s.sendto(nome_file.encode("utf-8"),indirizzo)           #eseguiamo l'encode
            dati = f.read(buffer)                                   #leggiamo il buffer

            while (dati):                                           #finchè ci sono dei dati da leggere
                if(s.sendto(dati,indirizzo)):                       #inviamo i dati al indirizzo in questione
                    print ("Invio in corso...")
                    dati = f.read(buffer)
            f.close()                                               #chiudiamo il file

        except FileNotFoundError:                                   #se il file non viene ricevuto laciamo un eccezione e rieseguaimo la funzione
            print("File non trovato.")
            chatClient()

if __name__ == "__main__":
    chatClient()