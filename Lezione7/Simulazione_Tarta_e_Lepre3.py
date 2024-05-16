# SFIDE AGGIUNTIVE:

# Energia o Stamina:

# Aggiungere una metrica di "energia" o "stamina" che diminuisce con ogni movimento e si ricarica in specifiche condizioni. 
# Fare in modo che le mosse che consumano più energia non possano essere eseguite se l'animale non ha abbastanza energia. 
# L'energia inziale per entrambi gli animali è 100.

# Nuove regole di movimento:

# - Tartaruga:
#     - Per la tartaruga, ogni volta che il numero generato indica una mossa ma non è possibile eseguirla per mancanza di energia, 
#       essa guadagna 10 di energia.
#     - Passo veloce (50% di probabilità): avanza di 3 quadrati e richiede 5 di energia.
#     - Scivolata (20% di probabilità): arretra di 6 quadrati e richiede 10 di energia. Non può andare sotto il quadrato 1.
#     - Passo lento (30% di probabilità): avanza di 1 quadrato e richiede 3 di energia.

# - Lepre:
#     - Riposo (20% di probabilità): non si muove e recupera 10 di energia. Non può superare l'energiza iniziale.
#     - Grande balzo (20% di probabilità): avanza di 9 quadrati  e richiede 15 di energia.
#     - Grande scivolata (10% di probabilità): arretra di 12 quadrati e richiede 20 di energia. Non può andare sotto il quadrato 1.
#     - Piccolo balzo (30% di probabilità): avanza di 1 quadrato e richiede 5 di energia.
#     - Piccola scivolata (20% di probabilità): arretra di 2 quadrati e richiede 8 di energia. Non può andare sotto il quadrato 1.


import random

posizione_T: int = 0
round: int = 1


#valori stamina tartaruga

stamina_tarta: int = 100


def tartaruga() -> int:
    x = random.randrange(1, 11)
    if x <= 5:
        return 3
    elif 6 <= x <= 7:
        return -6
    else:
        return +1



def posizione(tarta: int) -> list:
    circuito: list = []
    lunghezza_lista = 70
    circuito = ['_'] * lunghezza_lista
    if tarta < 0:
        tarta = 0
    elif tarta >= 70:
        tarta = 69
    
    circuito[tarta] = "T"
    return circuito


while posizione_T <= 69:
    print()
    print(f"Round {round}")
    move_tarta = tartaruga()

    if move_tarta == 3:
        stamina_tarta -= 5
    elif move_tarta == -6:
        stamina_tarta -= 10
    else:
        stamina_tarta -= 3

    stamina_usata_tarta: int = 100 - stamina_tarta

    if stamina_tarta < 0:
        move_tarta = 0
        stamina_tarta += 10
        print(" tarta no energie")
    
    posizione_T += move_tarta

    gara = posizione(posizione_T)

    lista_stamina = ["|"] * stamina_tarta
    lista_stamina_usata = ["_"] * stamina_usata_tarta
    print()
    
    print()
    print(" ".join(gara))
    print()
    print("STAMINA TARTA:  " + "".join(lista_stamina) +" " + " ".join(lista_stamina_usata) + f" {stamina_tarta}/100" )
    round += 1

    if posizione_T == 69:
        print("Tarta win")
        break
