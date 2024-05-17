# 1.
# 
# Scrivere il frammento di codice che cambi il valore intero memorizzato nella variabile x nel seguente modo:
# - se x è pari, deve essere diviso per 2;
# - se x è dispari deve essere moltiplicato per 3 e gli deve essere sottratto 1.

def transform(x: int) -> int:
    if x % 2 == 0:
        return int(x/2)
    elif x % 2 != 0:
        y = (x * 3) -1
        return int(y)
    
# Sviluppare una funzione in Python per calcolare lo stipendio lordo di ciascuno dei diversi impiegati. 
# L'azienda paga 10 dollari all'ora per le prime 40 ore di lavoro e paga "una volta e mezza" la paga oraria per tutte le ore di lavoro oltre le 40 ore.
#  
# Per ogni operaio, viene fornito il numero di ore che tale impiegato ha lavorato durante la settimana.
# La vostra funzione deve ricevere questa informazione per ogni impiegato e determinare e stampare lo stipendio lordo.

def calcola_stipendio(ore_lavorate: int) -> float:
    if ore_lavorate <= 40:
        y:float = ore_lavorate * 10.0
        return y
    elif ore_lavorate > 40:
        ore_straordinario: int = ore_lavorate - 40
        paga_ore_straordinario: float = ore_straordinario * 15.0
        paga: float = (40.0 * 10.0) + paga_ore_straordinario
        return paga
    

# Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
# a) 1, 2, 3, 4, 5, 6, 7
# b) 3, 8, 13, 18, 23
# c) 20, 14, 8, 2, -4, -10
# d) 19, 27, 35, 43, 51

def print_seq(): 
    
    a:list = [1, 2, 3, 4, 5, 6, 7]
    print("Sequenza a):")
    for x in a:
        print(x)
    
    print()

    b:list = [3, 8, 13, 18, 23]
    print("Sequenza b):")
    for x in b:
        print(x)
    print()

    c:list = [20, 14, 8, 2, -4, -10]
    print("Sequenza c):")
    for x in c:
        print(x)
    print()

    d:list = [19, 27, 35, 43, 51]
    print("Sequenza d):")
    for x in d:
        print(x)
    print()
    
    return

#Scrivere una funzione chiamata integerPower che, dati in input una base e un esponente, restituisca il risultato della potenza base^exponent. 
#Supporre che base sia un numero intero e che l'esponente sia un valore intero positivo e diverso da 0.
# 
#La funzione deve usare un ciclo come struttura di controllo per il calcolo del risultato.
#Non utilizzare nessuna funzione della libreria math!

def integerPower(base: int, esponente:int) -> int:
    x = base
    for y in range(1, esponente):
        base *= x
    return base

#Definire una funzione chiamata hypotenuse che calcoli la lunghezza dell'ipotenusa di un triangolo rettangolo. 
#La funzione deve ricevere due argomenti di tipo float (corrispondenti ai due lati del triangolo) e restituire l'ipotenusa come un float.
#Per calcolare l'ipotenusa, si può ricorrere al teorema di Pitagora.

def hypotenuse(lato_1:float, lato_2:float) -> float:
    x:float = (lato_1**2 + lato_2**2)**(1/2)
    return float(x)

# Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere, 
# ritorni un nuovo insieme senza i numeri specificati nella lista.

def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    for y in elements_to_remove:
        if y in original_set:
            original_set.remove(y)
    print(original_set)


#Scrivere la funzione chiamata seconds_since_noon che riceva il tempo espresso come tre argomenti interi 
#(ore, minuti e secondi) e restituisca il numero dei secondi da quando l'orologio "ha battuto le 12" l'ultima volta 
#(le ore 12, dunque, vengono considerate come orario di partenza, dunque, come uno zero).
#
#Ad esempio, alle ore 3:15:50 sono passate 3 ore, 15 minuti e 50 secondi, ovvero sono 
#passati 11750 secondi da quando l'orologio ha "battuto le 12" per l'ultima volta.
#
#Definire, poi, la funzione chiamata time_difference che prende come argomento due orari, entrambi 
#espressi mediante ore, minuti e secondi. La funzione time_difference deve usare la funzione seconds_since_noon per 
#calcolare la quantità di tempo in secondi tra due orari, entrambi contenuti entro un ciclo dell'orologio di 12 ore.
#
#Ad esempio, tra le ore 1:00 e 3:15:30 sono passati 8130 secondi.

def seconds_since_noon(num_1: int, num_2: int, num_3: int) -> int:
    sec_in_hours: int = num_1 * 3600
    sec_in_minuts: int = num_2 * 60
    sec_tot = sec_in_hours + sec_in_minuts + num_3
    return sec_tot

def time_difference(num_1:int, num_2:int, num_3:int, num_4:int, num_5:int, num_6:int) -> int:
    sec_1 = seconds_since_noon(num_1, num_2, num_3)
    sec_2 = seconds_since_noon(num_4, num_5, num_6)
    difference: int = sec_1 - sec_2
    return difference


# Si scriva una funzione in Python che simuli una palla che rimbalza calcolando la sua altezza 
# da terra in centimetri per ogni secondo, a mano a mano che il tempo passa su un orologio simulato.
# 
# Al tempo zero la palla comincia ad altezza zero e ha una velocità iniziale di 100 cm/s.
# 
# Dopo ogni secondo, il valore dell'altezza cambia, aggiungendo al valore corrente dell'altezza il valore della velocità corrente; 
# poi, il valore della velocità viene modificato, sottraendo 96 al valore della velocità corrente.
# 
# Dunque, dopo ogni secondo, si ha che
# 
# altezza = altezza + velocità
# velocità = velocità - 96.
#  
# Se il nuovo valore che si ottiene per l'altezza è inferiore a 0, si deve moltiplicare altezza e velocità per -0.5 per 
# simulare il rimbalzo. Dunque, per il rimbalzo, si avrà che
# 
# altezza= altezza*-0,5 
# velocità=velocità*-0,5.
# 
# Ci si fermi al quinto rimbalzo.
#  
# Per ogni secondo, la funzione deve stampare il tempo trascorso e l'altezza a cui si trova la palla in quel determinato secondo.
# Ad esempio, se al tempo 0, la palla si trova ad altezza 0 cm, allora la funzione stamperà:
#  
# "Tempo: 0 Altezza: 0"
#  
# Se avviene il rimbalzo, la funzione deve stampare il tempo trascorso e la parola "Rimbalzo!".
# Ad esempio, se il rimbalzo avviene al tempo 4, allora la funzione stamperà:
#  
# "Tempo: 4 Rimbalzo!"

def rimbalzo() -> None:
    
    tempo: int = 0
    altezza: float = 0.0
    velocita: float = 100.0
    rimbalzi: int = 0
    while rimbalzi <= 5:
        if altezza >= 0:
            print(f"Tempo: {tempo} Altezza: {altezza}") 
            altezza += velocita
            velocita -= 96
            tempo += 1
        elif altezza < 0:
            print(f"Tempo: {tempo} Rimbalzo!")
            altezza *= -0.5
            velocita *= -0.5
            rimbalzi += 1
            tempo += 1
