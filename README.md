# RANDOM_TESTS

![](docs_src/icon.svg)

## Introduzione
Questo script permette di generare liste di studenti 
casuali per le interrogazioni.

E' possibile avere volontari e scegliere il numero
di studenti per gruppo.
> Si consiglia di scegliere come numero di studenti per gruppo
> il numero di studenti che viene interrogato per volta.

> Se il numero di studenti non e' divisibile per il numero
> di studenti per gruppo l'ultimo gruppo avra'
> gli studenti rimanenti

## Indice
* [Guida all'uso](#guida-alluso)
    * [Studenti su file](#studenti-su-file)
    * [Studenti nel codice](#studenti-nel-codice)
* [Descrizione](#descrizione)
* [Test](#test)
* [Requisiti](#requisiti)
* [Changelog](#changelog)
* [Autore](#autore)

## Guida all'uso
Per utilizzare lo script ci sono due metodi:
* lista degli studenti su file
* lista di studenti nel codice

> Nota: se si ha installata la versione python 3.5 o precedente
> occorre installare la libreria ```python2-secrets``` eseguendo
> il comando ```pip install requirements.txt``` (file nella cartella ```randomtests```)
> o il comando ```pip install python2-secrets```

### Studenti su file
Passaggi:
1. Aprire lo script random_tests.py con un editor di testo
2. Modificare la variabile ```fromfile``` da ```fromfile = False``` a ```fromfile = True```
3. Modificare la variabile ```file_studenti```: specificare dove si trova il file con i nomi degli studenti
4. Se ci sono volontari aggiungerli alla lista ```volontari```
    > esempio: ```volontari = ["Giorgio", "Mario", "Francesca"]```
5. Scegliere quante persone verranno interrogate per gruppo attraverso la variabile ```persone_per_gruppo```
    > ad esempio: se si vogliono interrogare 3 persone per gruppo, impostare ```persone_per_gruppo = 3```
6. Salvare e eseguire lo script

### Studenti nel codice
Passaggi:
1. Aprire lo script random_tests.py con un editor di testo
2. Assicurarsi che la variabile ```fromfile``` sia impostata come segue: ```fromfile = False```
3. Modificare la variabile ```studenti```: aggiungere i nomi degli studenti
    > esempio: ```studenti = ["Giorgio", "Mario", "Francesca", "Nicola", "Giovanni"]```
4. Se ci sono volontari aggiungerli alla lista ```volontari```
    > esempio: ```volontari = ["Giorgio", "Mario", "Francesca"]```
5. Scegliere quante persone verranno interrogate per gruppo attraverso la variabile ```persone_per_gruppo```
    > ad esempio: se si vogliono interrogare 3 persone per gruppo, impostare ```persone_per_gruppo = 3```
6. Salvare e eseguire lo script

[Torna all'indice](#indice)

## Descrizione
Per leggere la documentazione dettagliata delle funzioni,
generata da sphinx, [cliccare qui](https://mario33881.github.io/random_tests/html/random_tests/random_tests.html).
> Nota: per generare la documentazione eseguire il comando ```make html``` (richiede sphinx installato)

RANDOM TESTS: Genera la lista degli studenti per le interrogazioni.

Se ```fromfile``` e' ```True``` viene usata la funzione
```extract_students()``` per creare il vettore con gli studenti,
altrimenti viene usato direttamente il vettore ```studenti```.

Il vettore ```volontari``` permette di aggiungere eventuali
volontari a inizio lista delle interrogazioni.

> l'ordine ha importanza, il primo studente nel vettore
> e' il primo interrogato

Poi viene usata la funzione ```gen_rnd_list()``` per ottenere
una lista casuale degli interrogati.

> Pesca un interrogato casuale continuamente finche' non li ha
> pescati tutti

La lista casuale viene usata per visualizzare
tanti studenti per gruppo quanti sono specificati
dalla variabile ```persone_per_gruppo```.

> il risultato e' "pipe-friendly": e' possibile
> utilizzare il pipe per mandare l'output su file da linea di comando

> Per assicurare l'unicita' degli studenti (non possono essere inseriti doppi)
> la funzione ```gen_rnd_list()``` usa la funzione ```check_unique()```.

> La funzione ```remove_blanks()``` si accorge se sono stati passati
> alunni "nulli/vuoti" (esempio: ```studenti = [" "]```) o numeri (```studenti = [1, 2, 3]```)

[Torna all'indice](#indice)

## Test
Random_tests e' testato utilizzando la libreria unittest.

Per la documentazione dei test:
* test di random_tests.py: [cliccare qui](https://mario33881.github.io/random_tests/html/test_random_tests/test_random_tests.html)

[Torna all'indice](#indice)

## Requisiti
* python 3
* libreria python2-secrets (per tutte le versioni python precedenti alla 3.6, quindi 3.5, 3.4,...)

[Torna all'indice](#indice)

## Changelog

**2020-04-03 01_01:** <br>
Primo commit

[Torna all'indice](#indice)

## Autore
Zenaro Stefano

[Torna all'indice](#indice)