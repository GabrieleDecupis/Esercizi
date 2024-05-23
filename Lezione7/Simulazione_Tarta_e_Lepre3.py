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

posizione_L: int = 0
posizione_T: int = 0
round: int = 1

#valori stamina tartaruga

stamina_tarta: int = 100
stamina_lepre: int = 100

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

def tartaruga() -> int:
    x = random.randrange(1, 11)
    if x <= 5:
        return 3
    elif 6 <= x <= 7:
        return -6
    else:
        return +1

def energie_lepre(move_lepre: int) -> int:
    if move_lepre == 0:
        stamina_round = -10  # modifica stamina_round in stamina_lepre_round
    elif move_lepre == 9:
        stamina_round = 15
    elif move_lepre == -12:
        stamina_round = 20
    elif move_lepre == 1:
        stamina_round = 5
    else:
        stamina_round = 8
    
    return stamina_round

def energie_tarta(move_tarta: int) -> int:
    if move_tarta == 3:
        stamina_round = 5  # modifica stamina_round in stamina_tarta_round
    elif move_tarta == -6:
        stamina_round = 10
    else:
        stamina_round = 3
    
    return stamina_round

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

while posizione_T <= 69:
    print()
    print(f"Round {round}\n")
    move_tarta = tartaruga()
    move_lepre = lepre()
    stamina_round_tarta = energie_tarta(move_tarta)
    stamina_round_lepre = energie_lepre(move_lepre)
    
    stamina_tarta -= stamina_round_tarta
    stamina_usata_tarta: int = 100 - stamina_tarta
    stamina_lepre -= stamina_round_lepre
    stamina_usata_lepre: int = 100 - stamina_lepre
    
    if stamina_tarta < 0:
        move_tarta = 0
        stamina_tarta += 10
        print(" tarta no energie")
    
    if stamina_lepre < 0:
        move_lepre = 0
        stamina_lepre += 10
        print(" lepre no energie")
    elif stamina_lepre > 100:
        stamina_lepre = 100
    
    posizione_T += move_tarta
    posizione_L += move_lepre

    gara = posizione(posizione_T, posizione_L)

    lista_stamina = ["|"] * stamina_tarta
    lista_stamina_usata_tarta = ["_"] * stamina_usata_tarta
    print()

    lista_stamina = ["|"] * stamina_lepre
    lista_stamina_usata_lepre = ["_"] * stamina_usata_lepre
    print()
    
    print()
    print(" ".join(gara))
    print()
    print("STAMINA TARTA:  " + "".join(lista_stamina) +" " + " ".join(lista_stamina_usata_tarta) + f" {stamina_tarta}/100\n" )
    print("STAMINA LEPRE:  " + "".join(lista_stamina) +" " + " ".join(lista_stamina_usata_lepre) + f" {stamina_lepre}/100\n" )
    round += 1

    if posizione_T >= 69:
        print("Tarta win!!")
    elif posizione_L >= 69:
        print("Lepre win!!")
    elif posizione_L >= 69 and posizione_T >= 69:
        print("IT'S A TIE BUT TORTOISE WINS! || VAY!!!")
