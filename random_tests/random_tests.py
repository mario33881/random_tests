"""
RANDOM_TESTS

Genera la lista degli studenti per le interrogazioni.

Se ``fromfile`` e' ``True`` viene usata la funzione
:func:`extract_students()` per creare il vettore con gli studenti,
altrimenti viene usato direttamente il vettore ``studenti``.

Il vettore ``volontari`` permette di aggiungere eventuali
volontari a inizio lista delle interrogazioni.

.. note:: l'ordine ha importanza, il primo studente nel vettore
   e' il primo interrogato

Poi viene usata la funzione :func:`gen_rnd_list()` per ottenere
una lista casuale degli interrogati.

.. note:: Pesca un interrogato casuale continuamente finche' non li ha
   pescati tutti

La lista casuale viene usata per visualizzare
tanti studenti per gruppo quanti sono specificati
dalla variabile ``persone_per_gruppo``.

.. note:: il risultato e' "pipe-friendly", e' possibile
   utilizzare il pipe per mandare l'output su file da linea di comando

.. note:: Per assicurare l'unicita' degli studenti (non possono essere inseriti doppi)
   la funzione :func:`gen_rnd_list()` usa la funzione :func:`check_unique()`.
"""

__author__ = "Zenaro Stefano"
__version__ = "2020-04-03 01_01"

import secrets  # metodo migliore per scelta random
import os       # usato per verificare esistenza file

boold = False     # True = visualizza messaggi di debug
fromfile = False  # True = usa file_studenti per ottenere gli studenti, altrimenti usa lista studenti

file_studenti = "example.txt"  # percorso file con studenti
studenti = []                  # lista studenti
volontari = []                 # lista volontari
persone_per_gruppo = 4         # numero persone nei gruppi


class NonUniqueStudentsError(Exception):
    """
    Errore lanciato quando vettore studenti contiene duplicati.
    """
    pass


class NonUniqueVolunteersError(Exception):
    """
    Errore lanciato quando vettore volontari contiene duplicati.
    """
    pass


class NoStudents(Exception):
    """
    Errore lanciato quando vettore studenti e' vuoto.
    """
    pass


def check_unique(t_vector):
    """
    Indica se t_vector ha valori unici.

    Un loop scorre gli elementi:
    se un elemento e' presente piu'
    di una volta nel vettore il check
    e' negativo.

    Se finisce il loop il check e' positivo.

    :param list t_vector: vettore di elementi
    :return check: booleano, se True gli elementi sono unici
    :rtype: bool
    """
    
    # default check positivo
    check = True

    # per ogni elemento del vettore
    for el in t_vector:
        # se l'elemento e' presente piu' di una volta
        if t_vector.count(el) > 1:
            if boold:
                print("Elemento duplicato: ", el)
                
            check = False  # il check e' negativo
            break          # termina check

    if boold and check:
        print("Niente duplicati")
        
    return check

    
def gen_rnd_list(t_vstudenti, t_volontari=[]):
    """
    Genera lista di interrogati casuali.

    La funzione salva la lista dei volontari
    nella lista degli interrogati,
    poi, all'interno di un loop, viene scelto
    casualmente un elemento di t_vstudenti.

    Se questo elemento non e' gia' nella lista
    degli interrogati (non e' stato pescato e non e' volontario)
    allora l'elemento viene inserito nella lista.

    Nel momento in cui il numero di elementi nella
    lista degli interrogati e' uguale al numero
    di studenti del vettore passato alla funzione
    sono uguali il loop termina.

    .. note:: per assicurarsi di non falsare la lista degli interrogati
       verra' controllata l'unicita' degli elementi in t_vstudenti
       e in t_volontari attraverso la funzione check_unique()
    
    :param list t_vstudenti: vettore con studenti
    :param list t_volontari: vettore studenti volontari
    :return lista_interrogati: vettore con studenti da interrogare
    :rtype: list
    """

    # se il vettore degli studenti t_vstudenti ha duplicati
    # la funzione da errore
    if not check_unique(t_vstudenti):
        raise NonUniqueStudentsError("Il vettore degli studenti ha duplicati")

    if len(t_vstudenti) == 0:
        raise NoStudents("Il vettore deve contenenere almeno uno studente")

    # se il vettore degli interrogati t_volontari ha duplicati
    # la funzione da errore
    if not check_unique(t_volontari):
        raise NonUniqueVolunteersError("Il vettore dei volontari ha duplicati")
    
    # aggiungo i volontari alla lista degli interrogati
    # (l'ordine resta invariato)
    lista_interrogati = t_volontari[:]

    if boold:
        print("Volontari: ", t_volontari)
        
    # continua fino al break
    while True:
        # scegli studente random
        random_student = secrets.choice(t_vstudenti)

        if boold:
            print("Scelto studente random:", random_student, end="")
            
        # se lo studente non appartiene alla lista degli interrogati,
        # (non e' stato pescato / non e' volontario) aggiungilo
        if random_student not in lista_interrogati:
            if boold:
                print(" - studente nuovo")
            lista_interrogati.append(random_student)

        else:
            if boold:
                print("")
                
        # quando le liste degli interrogati e degli studenti sono
        # uguali sono finiti gli studenti
        if len(lista_interrogati) == len(t_vstudenti):
            break

    if boold:
        print("Finito di generare lista studenti:", lista_interrogati)
        
    return lista_interrogati


def extract_students(t_filepath):
    """
    Estrae gli studenti dal file t_filepath.

    Apre il file t_filepath in modalita' lettura,
    scorre il file e recupera gli studenti.
    
	.. note:: gli studenti sono uno per riga

    :param str t_filepath: stringa, percorso file studenti
    :return studenti_infile: vettore con studenti del file
    :rtype: list
    """
    # usato per memorizzare gli studenti del file
    studenti_infile = []

    # apri il file in modalita' lettura
    with open(t_filepath, "r") as fin:
        # leggi la prima riga
        line = fin.readline()

        # loop delle righe fino a fine file
        while line != "":
            # ottieni dalla riga lo studente (togli "\n" e spazi)
            t_studente = line.strip()

            # aggiungi al vettore degli studenti lo studente
            studenti_infile.append(t_studente)

            # passa alla riga successiva
            line = fin.readline()

    return studenti_infile


def remove_blanks(t_vector):
    """
    Restituisce il vettore <t_vector> senza stringhe vuote/nulle.

    La funzione scorre il vettore e controlla che ogni elemento
    non sia una stringa nulla ("") o vuota ("    ")

    :param list t_vector: vettore di stringhe
    :return noblanks_vector: vettore t_vector senza stringhe vuote/nulle
    :rtype: list
    """
    # vettore che contiene stringhe NON nulle/vuote
    noblanks_vector = []

    # per ogni elemento in <t_vector>
    for el in t_vector:
        # se l'elemento (a cui e' stato rimosso "\n", "\t", " ")
        # non e' stringa vuota
        if el.strip() != "":
            # aggiungilo alla lista <noblanks_vector>
            noblanks_vector.append(el.strip())

    return noblanks_vector


if __name__ == "__main__":

    if boold:
        print("Inizio programma")
        print("-" * 50)
        print("Ottengo la lista random\n")

    # ci deve essere almeno una persona per gruppo:
    if persone_per_gruppo < 1:
        print("Un gruppo e' formato da almeno una persona")
        exit(2)
        
    # se la lista studenti proviene da file, estrai gli studenti
    # dal file
    if fromfile:
        if not os.path.isfile(file_studenti):
            print("File non esistente: '{}'".format(file_studenti))
            exit(1)
        studenti = extract_students(file_studenti)

    try:
        # assicurati che non ci siano stringhe vuote/nulle
        # > Nota: i numeri lanciano un AttributeError con strip()
        nonblank_studenti = remove_blanks(studenti)
        nonblank_volontari = remove_blanks(volontari)

        # lista di studenti random
        studenti_random = gen_rnd_list(nonblank_studenti, nonblank_volontari)

        i = 1                    # numero per riconoscere quando cambiare gruppo
        n_gruppo = 1             # numero del gruppo
        gruppo_cambiato = True   # True se si e' passati al gruppo successivo (o se e' il primo gruppo)

        # loop degli studenti
        for studente in studenti_random:
            # se e' cambiato il gruppo, visualizza "\nGruppo <n_gruppo>: "
            if gruppo_cambiato:
                print("\nGruppo ", n_gruppo, ": ", end="")
                gruppo_cambiato = False

            # visualizza "<studente> | "
            print(studente, "| ", end="")

            # quando <i> e' divisibile per il numero delle persone
            # per gruppo, cambia gruppo
            if i % persone_per_gruppo == 0:
                n_gruppo += 1           # nuovo gruppo: incrementa il numero del gruppo
                gruppo_cambiato = True  # e a inizio loop visualizzalo

            # incrementa il contatore degli studenti
            i += 1

        # vai a capo dopo l'ultimo studente
        print("")

    except NoStudents:
        print("Deve essere presente almeno uno studente")

    except NonUniqueVolunteersError:
        print("Alcuni volontari sono presenti numerose volte")

    except NonUniqueStudentsError:
        print("Alcuni studenti sono presenti numerose volte")

    except AttributeError:
        print("E' stato passato un numero all'interno del vettore volontari/studenti")

    if boold:
        print("\nFine generazione gruppi")
        print("-" * 50)
        print("Fine programma")
