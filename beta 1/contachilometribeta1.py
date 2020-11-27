#Ideato e Scritto da Marco Venerandi,ogni uso è libero finche Marco venerandi o Pamafa Software saranno accreditati della creazione.
#Calcola approsimativamente il guadagno netto del rimborso chilometri
#richiede :chilometri,euro\km
#può salvare infiniti percori Es.autostrada a4 da svincolo x a svincolo y

import os
import sys
import time
from playsound import playsound
d = {}

def clear():
    if os.name == 'nt':
        _ = os.system("cls")

def crea_file():
    b = 1
    nome = ("mese" + str(b) + ".txt")
    a = 1
    os.makedirs("FileCalcolaChilometri")   #crea la cartella dei file e la imposta come cartella di lavoro
    os.chdir("FileCalcolaChilometri")
    try:
        file = open("percorsi.txt", "w")                #crea il file dove verranno inseriti percorsi e i valori di km
    except PermissionError:
        while True:
            if a > 100 :   #conta il numero di volte che prova se è possibile scrivere file,dopo 100 tentativi 
                print ("ERRORE CRITICO CREAZIONE FILE")
                input("Premi invio per uscire...")
                exit()
            a += 1
            print ("Errore, ", a, "esimo tentativo..")
            try:
                file = open("percorsi.txt", "w")
            except PermissionError:
                continue
            break
    for f in range(12):
        filem = open(nome, "w")
        filem.close()
        b += 1
        nome = ("mese" + str(b) + ".txt")
    
    file = open("percorsi.txt", "w")    #se non incotra errori crea il file
    file.write("non modificare 123456789abc")
    file.close()
    file = open("percorsi.txt", "r").readlines()
    if file[0] == "non modificare 123456789abc" : #controlla una stringa di prova,in caso di errore non interrompe il programma !questo puo causare interruzioni inaspettate!
        return True
    else:
        return False
    

 
def calcolo():
    km = 0
    km_tot = 0                      #dichiarazione varibili essenziali
    euro = 0
    print ("Inserire il totale o ogni singolo valore, quando terminato inserire 'x' \n")
    while True:
        km = input("Inserire il numero di Km in numero decimale separato dal '.' Es 185.50  : ")
        if km == "x" or km == "X" :                     #controllo parametro di uscita ciclo
            print ("Fine inserimento chilometri.\n")
            break
        try:                                                #parametro di controllo per inserimenti errati
            km = float(km)
        except ValueError:
            print (" Inserire Solo NUMERI decimali o 'x'.  \n")
            print ("\n")
            continue
        km = float(km)
        km_tot = (km + km_tot)
    clear()
    while True:
        euro = input("inserire il rimborso in euro decimali usando il '.' come separatore  per 1 chilometri Es 1.25  : ")
        try:                                                #parametro di controllo per inserimenti errati
            euro = float(euro)
        except ValueError:
            print (" Inserire Solo NUMERI decimali  \n")
            print ("\n")
            continue
        break
    euro = float(euro)
    risultato = (km_tot * euro)                                 #calcolo effettivo
    return risultato


def agg_percorso(nome, km):             #aggiunge i percorsi al file di testo
    km = str(km)
    clear()
    print ("Salvare il percorso  ", nome, "  Lungo : ", km, "   chilometri? ")  #se la risposta è si aggiunge due righe di testo al file
    si_no = input("s     n    ")
    if si_no == ("s") :
        file = open("percorsi.txt", "a")
        file.write("\n" + nome)
        file.write("\n" + km)
        file.close()
        return ("Fatto")

    else:
        return ("Operazione Annullata")


def carica_percorsi():
    file = open("percorsi.txt", "r").readlines()        #carica il file creando una lista con tutti i valori
    dimensione = len(file) - 1
    a = 0                       #imposto a ad 0 ,segna il numero di iterazioni che sono state eseguite
    d = {}                      #creazione dizionario
    i = 1                       #Imposto valore indice a 1 per scartare il valore 0 che è la stringa di controllo
    while a != dimensione / 2 :     #deve procedere fino a svolgere la metà dei valori,perchè viene inserito una voce nel dizionario ogni 2 valori (nome,km)
        d[file[i]] = file[i + 1]
        i += 2
        a += 1
    return d
        

def menu(dpercorsi):
    print ("Calcola Il rimborso dei Km\n")
    print ("'a'  Calcolo Mensile               'b'  Calcolo Istantaneo")
    print ("'c'  Aggiungere dei percorsi fissi                 'x' Per chiudere in sicurezza ")
    print ("'s' Crediti")
    scelta = input("segli una delle seguenti opzioni: ")
    clear()
    if scelta == "a" :
        return calcolo_mensile(dpercorsi)
    elif scelta == "b" :
        print ("Il rimborso totale netto dovrebbe ammontare a :  ", calcolo()) #lancia calcolo()
        input("Premi invio per proseguire...")
        return inizio()
    elif scelta == "c" :
        nome = input("Inserire il nome del percorso da salvare:  ")
        while True:
            km = input("Inserire il numero di Km in numero decimale separato dal '.' Es 185.50  : ")
            try:                                                #parametro di controllo per inserimenti errati
                km = float(km)
            except ValueError:
                print (" Inserire Solo NUMERI decimali \n")
                print ("\n")
                continue
            break
        print (agg_percorso(nome, km))          # lancia aggiungi percorso con i parametri appena dati
        input("Premi invio per proseguire...")
        return inizio() #ritorna a inizio() e non a menu() perchè deve ricaricare nel dizionario i nuovi dati.
    elif scelta == "x":
        clear()
        print("\nGrazie per aver usato il mio Programma!")
        input("premi invio per uscire..")
        exit()
           
    elif scelta == "s":
        global origine
        clear()
        os.chdir(origine)
        playsound("a.mp3", False)
        playsound("b.wav", False)
        print ("Pa")
        time.sleep(0.6)
        playsound("b.wav", False)
        print ("   Ma")
        time.sleep(0.6)
        playsound("b.wav", False)
        print ("      Fa")
        time.sleep(1)
        playsound("c.wav", False) 
        print ("         SOFTWARE")
        time.sleep(1.2)
        print()
        print("          Designer Master")
        print("          Marco Venerandi")
        time.sleep(1.2)
        print()
        print("          Program Group Leader")
        print("           Marco  Venerandi")
        time.sleep(1.2)
        print()
        print("          Beta Tester")
        print("          ???????????")
        time.sleep(1.2)
        print()
        input("grazie,premi invio per uscire..")
        exit()
            
        
        
        
        

def inizio():
    global origine
    os.chdir(origine) #imposta come cartella di lavoro quella dove è situato lo script per poter verificare se esiste la cartella dei file(!!altrimenti sarebbe dentro alla cartella dei file e non potrebe verificarne lesistenza!!)
    clear()
    if os.path.isdir("FileCalcolaChilometri") == True:
        os.chdir("FileCalcolaChilometri")
        verifica_permessi()     #verifica la possibilita di leggere il file
        d = carica_percorsi() #dizionario che contiene i percorsi
        return menu(d)
           
    print("creazione file necessari....")
    creazione = crea_file()
    if creazione == True :
        print ("Finito!")
        clear()
        return inizio()
    elif creazione == False:
       print ("OPS! Qualcosa è andato storto")
       return inizio()



def verifica_permessi():
    try:                                        # verifica di lettura file
        file = open("percorsi.txt", "r").readlines()
    except PermissionError:
        print ("OPS! Qualcosa è andato storto")
        input("Premi invio per uscire...")
        exit()
    
        

def calcolo_mensile(dpercorsi):
    clear()
    km_tot = 0       #creazioni variabili e dizionari essenziali
    subtotale = 0
    numpercorsi = {}
    d = dpercorsi
    mese = time.strftime("%m")
    print ("Calcolo Km del mese,(Crea un file con i vari totali e sub totali cosi da facilitare l'invio)")
    time.sleep(4)
    if mese == "1" or mese == "3" or mese == "5" or mese == "7" or mese == "8" or mese == "10" or mese == "12":
        lunghezzamese = 31
    elif mese == "2":
        lunghezzamese = 28    #parametri per la durata del mese
    else:
        lunghezzamese = 30

    while True:
        clear()
        gpartenza = input("Per Iniziare inserimento dal giorno attuale digita x, altrimenti digita il numero del giorno:  ")
        if gpartenza == "x":
            giorno = time.strftime("%e")
            break   
        try:                            #parametro di controllo per inserimenti errati
            prova = float(gpartenza)
        except ValueError:
            print (" Inserire una data numerica \n")
            print ("\n")
            time.sleep(1)
            continue
        if float(gpartenza) > lunghezzamese :
            print ("La data non può essere più di ", lunghezzamese)
            time.sleep(1)
            continue
        elif float(gpartenza) <= 0 :                                               #controlla che la data inserita non sia minore uguale a 0 e non sia più del mese
            print (" La data non può essere 0 o di meno!")
            time.sleep(1)
            continue
        giorno = int(gpartenza)
        break
    while True:
        while True:
            clear()
            a = 1
            for i in d.keys():
                numpercorsi[a] = i   #crea il dizionario con chiave semplice da digitare e con valore la chiave del dizionario dei percorsi
                print (a, ":   ", numpercorsi[a])
                a += 1
            percorsoscelto = input("digitare il percorso o i percorsi fatti il giorno " + str(giorno) + "  del mese : " + mese + "  uno per volta\ndigitare 'x' per passare al giorno seguente. \nse si vuole terminare subito digitare 'z' :  ")  #aggiungere paraetri sicurezza input e parametro uscita inserimento dati
            if percorsoscelto == "x":  #stampa su file il totale del giorno,azzera il totale gionagliero ed esce dal loop
                file = open("mese" + mese + ".txt", "a")
                file.write("\n TOTALE DEL GIORNO  " + str(giorno) + " : " + str(km_tot) + " Km")
                file.close()
                subtotale += km_tot
                km_tot = 0
                break
            elif percorsoscelto == "z":             #chiusura programma e stampa su file output totale del giono e sub totale inserimenti
                subtotale += km_tot
                file = open("mese" + mese + ".txt", "a")
                file.write("\n TOTALE DEL GIORNO  " + str(giorno) + " : " + str(km_tot) + " Km")
                file.write("\n Sub totale:  " + str(subtotale))
                file.write("\n DATI INSERITI IL " + time.strftime("%e"))
                file.close()
                input("Output salvato nel file del mese,premi invio per continuare...")
                return inizio()
            try:                            #parametro di controllo per inserimenti errati
                test = float(d[numpercorsi[float(percorsoscelto)]])
            except ValueError:
                print (" Inserire Solo i Numeri dei Percorsi \n")
                print ("\n")
                continue
            att = float(d[numpercorsi[float(percorsoscelto)]])
            km_tot = km_tot + float(att) #aggiunge il km del percorso scelto al totale giornagliero, stampa su file il percorso il giorno e la sua lunghezza
            file = open("mese" + mese + ".txt", "a")
            file.write("\nil Giorno" + str(giorno) + " è stato percorso  " + numpercorsi[float(percorsoscelto)] + "  Lungo: " + d[numpercorsi[float(percorsoscelto)]])
            file.close()

        giorno = int(giorno)  # finito il loop controlla se il giorno è lultimo del mese,in caso positivo interrompe
        if giorno == lunghezzamese:
            break
        giorno +=  1
        
    clear()
    file = open("mese" + mese + ".txt", "a")
    file.write("\n Sub totale:  " + str(subtotale))
    file.write("\n DATI INSERITI IL " + time.strftime("%e"))
    file.close()
    input("Output salvato nel file del mese,premi invio per continuare...")
    return inizio()
origine = os.getcwd()
inizio()
