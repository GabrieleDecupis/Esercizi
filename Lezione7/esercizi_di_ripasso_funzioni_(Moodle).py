# esercizio 1
# Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario. 
# Il dizionario contiene elementi da rimuovere come chiavi e il numero di volte che devono essere rimossi come valori.

# For example:

# print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2})) risultato [1, 3, 4]

# print(rimuovi_elementi([], {2: 1})) risultato []

def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    counter = 0
    lista_nuova = lista.copy()
    for k,v in da_rimuovere.items():
        while v > counter:
            if k in lista:
                lista_nuova.remove(k)
                counter += 1
            else:
                break
    
    return lista_nuova


#esercizio 2
#
#Scrivi una funzione che prenda in input una lista di dizionari che rappresentano voti di studenti e aggrega 
#i voti per studente in un nuovo dizionario.
#
#For example:
#
#print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))
#
#risultato:
#
#{'Alice': [90, 85], 'Bob': [75]}

def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    new_dict = {}
    for x in voti:
        nome_studente = x["nome"]
        voto_studente = x["voto"]
        if nome_studente in new_dict:
            new_dict[nome_studente].append(voto_studente)
        else:
            new_dict[nome_studente] = [voto_studente]
    
    return new_dict

# esericizio 3

# Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un nuovo dizionario con solo 
# i prodotti che hanno un prezzo superiore a 20, scontati del 10%.
# 
# For example:
# 
# print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0})) risultato: {'Zaino': 45.0, 'Quaderno': 19.8}

def filtra_e_mappa(prodotti: dict[str:float]) -> list[str:float]:
    prodotti_scontati: dict = {}
    for k,v in prodotti.items():
        if v > 20:
            prodotti_scontati[k] = v
        else:
            continue
    for k,v in prodotti_scontati.items():
        new_v: float = v - ((v * 10)/100)
        prodotti_scontati[k] = new_v        
    return prodotti_scontati


#PARTE 1
#Scrivi una funzione chiamata create_contact() che accetta il nome e cognome, e-mail (facoltativo) e numero di telefono (facoltativo). 
#La funzione dovrebbe restituire un dizionario con i dettagli del contatto.
#       contact = create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787)
#               {'profile': 'Mario Rossi', 'email': 'mario.rossi@gmail.com', 'telefono': 788787}
#PARTE 2
#Scrivi una funzione chiamata update_contact() che accetta il dizionario creato, il nome e cognome del contatto da aggiornare, 
#e il dettaglio facoltativo da aggiornare. Questa funzione dovrebbe aggiornare il dizionario del contatto.

def create_contact(name: str, email: str=None, telefono: int=None) -> dict:
    profilo: dict = {}
    profilo["profile"] = name
    profilo["email"] = email
    profilo["telefono"] = telefono

    return profilo

def update_contact(dictionary: dict, name: str, email: str =None, telefono: int=None) -> dict:
    for k,v in dictionary.items():
        if name is not None:
            dictionary["profile"] = name
        if email is not None:
            dictionary["email"] = email
        if telefono is not None:
            dictionary["telefono"] = telefono

    return dictionary

            