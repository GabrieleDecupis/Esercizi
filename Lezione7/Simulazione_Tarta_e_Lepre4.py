# 3. Ostacoli e Bonus
# 
# Sulla pista di gara sono presenti alcuni ostacoli e bonus a posizioni fisse, che influenzano direttamente il 
# movimento degli animali quando vengono calpestati. Gli ostacoli causano uno slittamento all'indietro, 
# mentre i bonus offrono un avanzamento extra.
# 
# Dettagli Implementativi:
# 
# - Ostacoli:
# 
# Posizionati a intervalli regolari sulla pista (es. ai quadrati 15, 30, 45), gli ostacoli riducono la 
# posizione dell'animale di un numero specificato di quadrati (es: -3, -5, -7). 
# Gli ostacoli sono rappresentati da un dizionario che mappa le posizioni degli ostacoli sul percorso (chiave) ed i relaviti effetti (valore). 
# Assicurarsi che nessun animale retroceda al di sotto del primo quadrato a seguito di un ostacolo.
# 
# - Bonus:
# 
# Dislocati strategicamente lungo la corsa (es. ai quadrati 10, 25, 50), i bonus aumentano la posizione dell'animale di un 
# numero determinato di quadrati (es: 5, 3, 10). 
# I bonus sono rappresentati da un dizionario che mappa le posizioni dei bonus sul percorso (chiave) ed i relaviti effetti (valore). 
# Consentire agli animali di beneficiare pienamente dei bonus, ma non oltrepassare il traguardo.


ostacoli: dict = {15: -3, 30: -6, 45: -9, 60: -12}
bonus: dict = {10: 2, 20: 4, 30: 6, 40: 8, 50: 10, 60: 12}

import random

posizione_T = 0
posizione_H = 0
round = 1

def tartaruga() -> int:
    x = random.randrange(1, 11)
    if x <= 5:
        return 3
    elif 6 <= x <= 7:
        return -6
    else:
        return +1

def lepre() -> int:
    x = random.randrange(1, 11)
    if 1 <= x <= 2:
        return 0
    elif 3 <= x <= 4:
        return +9
    elif x == 5:
        return -12
    elif 6 <= x <= 8:
        return 1
    elif 9 <= x <= 10:
        return -2

def posizione(tarta:int, lepre:int):
    circuito: list = []
    lunghezza_lista = 70
    circuito = ['_'] * lunghezza_lista

    if tarta < 0:
        tarta = 0
    elif tarta >= 70:
        tarta = 69
    
    circuito[tarta] = "T"

    if lepre < 0:
        lepre = 0
    elif lepre >= 70:
        lepre = 69
    
    circuito[lepre] = "H"

    if tarta == lepre:
        circuito[lepre] = "OUCH"
    
    return circuito

print("BANG !!!!! AND THEY'RE OFF !!!!!")

while posizione_H <= 69 and posizione_T <= 69:

    print(f"ROUND {round}\n")

    move_tartaruga = tartaruga()
    move_lepre = lepre()

    posizione_T += move_tartaruga
    posizione_H += move_lepre

    for k,v in ostacoli.items():
        if posizione_T == k:
            posizione_T -= v
            print("T get a malus\n")
        elif posizione_H == k:
            posizione_H -= v
            print("H get a malus\n")
    
    for k,v in bonus.items():
        if posizione_T == k:
            posizione_T += v
            if posizione_T > 69:
                posizione_T -= v
                print("T get a bonus but is out of range\n")
            else:
                print("T get a bonus")
        elif posizione_H == k:
            posizione_H += v
            if posizione_H > 69:
                posizione_H -= v
                print("H get a bonus but is out of range")
            else:
                print("H get a bonus")


    gara = posizione(posizione_T, posizione_H)
    
    if posizione_T >= 69:
        print(" ".join(gara))
        print()
        print("TORTOISE WINS! || YAY!!!")
        break
    
    if posizione_H >= 69:
        print(" ".join(gara))
        print()
        print("HARE WINS! || YAY!!!")
        break
    
    if posizione_H >= 69 and posizione_T >= 69:
        print(" ".join(gara))
        print()
        print("IT'S A TIE BUT TORTOISE WINS! || VAY!!!")
        break
    
    print(" ".join(gara)+ "\n")

    round += 1