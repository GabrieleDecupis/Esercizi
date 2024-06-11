# Obiettivo:
# Implementare una classe Media che rappresenti un media generico (ad esempio, un film o un libro) e una classe derivata Film che 
# rappresenti specificamente un film. Gli studenti dovranno anche creare oggetti di queste classi, aggiungere valutazioni e visualizzare 
# le recensioni.

# Specifiche della Classe Media:
 
# Attributi:
# - title (stringa): Il titolo del media.
# - reviews (lista di interi): Una lista di valutazioni del media, con voti compresi tra 1 e 5.

# Metodi:
# - set_title(self, title): Imposta il titolo del media.
# - get_title(self): Restituisce il titolo del media.
# - aggiungiValutazione(self, voto): Aggiunge una valutazione alla lista delle recensioni se è valida (tra 1 e 5).
# - getMedia(self): Calcola e restituisce la media delle valutazioni.
# - getRate(self): Restituisce una stringa che descrive il giudizio medio del media basato sulla media delle valutazioni.
# - ratePercentage(self, voto): Calcola e restituisce la percentuale di un voto specifico nelle recensioni.
# - recensione(self): Mostra un riassunto delle recensioni e delle valutazioni del media, stampando il titolo, il voto medio, 
#   il giudizio e le percentuali di ciascun voto. Esempio di riassunto:
 
# Titolo del Film: The Shawshank Redemption
# Voto Medio: 3.80
# Giudizio: Bello
# Terribile: 10.00%
# Brutto: 10.00%
# Normale: 10.00%
# Bello: 30.00%
# Grandioso: 40.00%

# Si verifichi il funzionamento scrivendo un codice che crei almeno due oggetti di tipo Film, aggiunga a ognuno dei due almeno dieci 
# valutazioni e richiami il metodo recensione().

class Media:
    def __init__ (self, title: str):
        self.title = title
        self.reviews: list[int] = []
    
    def set_title(self, title: str):
        self.title = title

    def get_title(self):
        return f"Titolo del film: {self.title}"
    
    def aggiungiValutazione(self, voto: int):
        if 1<= voto <= 5:
            self.reviews.append(voto)
    
    def getMedia(self):
        return round(sum(x for x in self.reviews) / len(self.reviews), 1)
    
    def getRate(self):
        x = Media.getMedia(self)
        if x <= 2:
            return "Giudizio: Terribile"
        if 2 < x <= 3:
            return "Giudizio: Brutto"
        if 3 < x <= 4:
            return "Giudizio: Normale"
        if 4 < x < 4.5:
            return "Giudizio: Bello"
        else:
            return "Giudizio: Grandioso"
    
    def ratePercentage(self, voto: int):
        counter = 0
        for x in self.reviews:
            if x == voto:
                counter += 1
        
        percentuale = round((counter * 100) / len(self.reviews), 1)
        if voto == 1:
            return f"Terribile: {percentuale}%"
        if voto == 2:
            return f"Brutto: {percentuale}%"
        if voto == 3:
            return f"Normale: {percentuale}%" 
        if voto == 4:
            return f"Bello: {percentuale}%"
        if voto == 5:
            return f"Grandioso: {percentuale}%"

    def recensione(self):
        return f"{Media.get_title(self)}\nVoto Medio: {Media.getMedia(self)}\n{Media.getRate(self)}\n{Media.ratePercentage(self, 1)}\n{Media.ratePercentage(self, 2)}\n{Media.ratePercentage(self, 3)}\n{Media.ratePercentage(self, 4)}\n{Media.ratePercentage(self, 5)}"


# film1 = Media("il pianeta del tesoro")
# film1.aggiungiValutazione(4)
# film1.aggiungiValutazione(5)
# film1.aggiungiValutazione(5)
# film1.aggiungiValutazione(5)
# film1.aggiungiValutazione(5)
# film1.aggiungiValutazione(5)
# film1.aggiungiValutazione(5)
# film1.aggiungiValutazione(5)
# film1.aggiungiValutazione(5)
# film1.aggiungiValutazione(5)
# film1.aggiungiValutazione(5)
# film1.aggiungiValutazione(4)
# film1.aggiungiValutazione(3)
# film1.aggiungiValutazione(4)
# film1.aggiungiValutazione(4)
# film1.aggiungiValutazione(4)
# film1.aggiungiValutazione(4)
# film1.aggiungiValutazione(4)
# film1.aggiungiValutazione(3)
# film1.aggiungiValutazione(3)
# film1.aggiungiValutazione(3)
# film1.aggiungiValutazione(3)
# film1.aggiungiValutazione(3)
# film1.aggiungiValutazione(3)
# film1.aggiungiValutazione(3)
# film1.aggiungiValutazione(3)
# film1.aggiungiValutazione(3)
# print(film1.recensione())