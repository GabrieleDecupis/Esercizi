# SFIDE AGGIUNTIVE:
# 
# 1. Variabilità Ambientale:
# 
# Introdurre fattori ambientali che possono influenzare la corsa, come il meteo.
# Ad esempio, la pioggia può ridurre la velocità di avanzamento o aumentare la probabilità di scivolate per entrambi i concorrenti. 
# Implementare un sistema dove le condizioni 'soleggiato' e 'pioggia' cambiano dinamicamente ogni 10 tick dell'orologio.
#  
# Modificatori mossa:
# 
# - La Tartaruga in caso di pioggia subisce penalità -1 su ogni mossa. In caso di sole non subisce variazioni.
# - La Lepre in caso di pioggia subisca una penalità -2 su ogni mossa. In caso di sole non subisce variazioni.

import random

posizione_T = 0
posizione_H = 0
round = 10
meteo: list = []

for x in range(0, 1000, 2):
    meteo.append(x)

def tartaruga_sole() -> int:
    x = random.randrange(1, 11)
    if x <= 5:
        return 3
    elif 6 <= x <= 7:
        return -6
    else:
        return +1
    
def tartaruga_pioggia() -> int:
    x = random.randrange(1, 11)
    if x <= 5:
        return 2
    elif 6 <= x <= 7:
        return -7
    else:
        return 0
    
def lepre_sole() -> int:
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

def lepre_pioggia() -> int:
    x = random.randrange(1, 11)
    if 1 <= x <= 2:
        return -2
    elif 3 <= x <= 4:
        return +7
    elif x == 5:
        return -14
    elif 6 <= x <= 8:
        return -1
    elif 9 <= x <= 10:
        return -4

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

while posizione_H <= 69 and posizione_T <= 69:

    print(f"ROUND {round}\n")

    if round // 10 in meteo:
        print("E' spuntato il sole!!\n")
        move_tartaruga = tartaruga_sole()
        move_lepre = lepre_sole()
    else:
        print("Oh no!! Sta piovendo!!\n")
        move_tartaruga = tartaruga_pioggia()
        move_lepre = lepre_pioggia()
    
    posizione_T += move_tartaruga
    posizione_H += move_lepre

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

