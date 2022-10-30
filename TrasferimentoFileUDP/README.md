#Es Trasferimento file con protocollo UDP

In questo esercizio l'obettivo è quello di trasferire un file tramite il protocollo UDP.
Esso non prevede, a differenza del protocollo TCP, la creazione di una connessione tra mittente e destinatario. Questo fatto diminuisce notevolemente la velocità di trasmissione dei pacchetti a discapito dell' affidabilità.

##Client

Nel nostro caso, per quanto riguarda il lato client, abbiamo definito una funzione dove inizializziamo il socket, impostiamo l'host, la porta e la dimesione del buffer.
Successivamente, all'interno di un try-catch, apriamo il file da leggere in modalità "rb" (lettura binaria), ne eseguiamo l'encode e leggiamo il buffer. Se il file è stato trvato, il, file viene inviato in pacchetti che variano in base alla dimensione del buffer, altrimenti viene lanciata un eccezione FileNotFoundError e viene richiamata la funzione.

##Server

Per quanto riguarda il lato server, le prime righe (socket, porte indirizzo, ecc...) sono analoghe.
Successivamente, tramite la funzione recvfrom, leggiamo il buffer, dopodiche creiamo una copia del file inviato, aprendolo in modalità "wb" (scrittura binaria).
All'interno di un try-catch, tramite un ciclo while,leggiamo il buffer fino al suo svuotamento e impostaiamo un timeout: allo scadere del timeout o alla completa ricezione dei dati, la scrittura si interrompe e il file si chiude.