# Gestione di un magazzino
# 
# Scrivi un programma in Python che gestisca un magazzino. Il programma deve permettere di aggiungere prodotti al magazzino, 
# cercare prodotti per nome e verificare la disponibilità di un prodotto.
# 
# Definisci una classe Prodotto con i seguenti attributi:
# - nome (stringa)
# - quantità (intero)
#  
# Definisci una classe Magazzino con i seguenti metodi:
# 
# - aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.
# - cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
# - verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.

# marco.cascio@unitelmasapienza.it


class Prodotto:
    def __init__(self, nome_prodotto: str, quantità_prodotto: str) -> None:
        self.nome_prodotto = nome_prodotto
        self.quantità_prodotto = quantità_prodotto
    


class Magazzino:
    def __init__(self) -> None:
        self.prodotti: list[Prodotto] = []
    
    def aggiungi_prodotto(self, prodotto: Prodotto):
        if prodotto not in self.prodotti:
            self.prodotti.append(prodotto)
    
    def cerca_prodotto(self, nome_prodotto: str):
        for prodotto_in_magazzino in self.prodotti:
            if nome_prodotto == prodotto_in_magazzino.nome_prodotto:
                return f"{nome_prodotto} è presente nel magazzino"
        return f"{nome_prodotto} non è presente nel magazzino"
    
    def verifica_disponibilità(self, nome_prodotto: str):
        for prodotto_in_magazzino in self.prodotti:
            if nome_prodotto == prodotto_in_magazzino.nome_prodotto and prodotto_in_magazzino.quantità_prodotto != 0:
                return f"{nome_prodotto} è disponibile in queste quantità: {prodotto_in_magazzino.quantità_prodotto}"
        return f"{nome_prodotto} non è disponibile nel magazzino"
    
    def __str__(self) -> str:
        return self.prodotti 
    

    


        
        
