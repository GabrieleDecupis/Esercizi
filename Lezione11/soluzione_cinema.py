# Sistema di Prenotazione Cinema
# 
# Sviluppa un sistema in Python che gestisca le prenotazioni per un cinema. Il cinema ha diverse sale, ognuna con un diverso 
# film in programmazione. Gli utenti possono vedere quali film sono disponibili e prenotare posti per un determinato spettacolo.
# 
# Classi:
#     - Film: Rappresenta un film con titolo e durata.
#     - Sala: Rappresenta una sala con numero identificativo, film attualmente in programmazione, posti totali, posti prenotati.
#     - Cinema: Gestisce le operazioni legate alla gestione delle sale.
#
# Metodi sala:
#     - prenota_posti(num_posti): Prenota un certo numero di posti nella sala, se disponibili. 
#       Restituisce un messaggio di conferma o di errore.
#     - posti_disponibili(): Restituisce il numero di posti ancora disponibili nella sala.
# 
# Metodi cinema:
#     - aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
#     - prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta di prenotare posti. Restituisce un messaggio di stato.
# 
# Test case:
# 
# - Un gestore del cinema configura le sale aggiungendo i film e i dettagli dei posti.
# 
# - Un cliente sceglie un film e prenota un certo numero di posti.
# 
# - Il sistema verifica la disponibilità e conferma o rifiuta la prenotazione.


class Film:

    def __init__(self, titolo: str, durata: int) -> None:
        self.titolo = titolo
        self.durata = durata

class Sala:

    def __init__(self, numero_sala: int, film: Film, posti_totali: int):
        self.numero_sala = numero_sala
        self.film = film
        self.posti_totali = posti_totali
        self.posti_prenotati = 0 # essendo una cosa costante per tutte le istanze posso evitare di metterla come attribbuto e metterla così
    
    def prenota_posti (self, num_posti: int) -> str:
        if self.posti_totali - self.posti_prenotati >= num_posti:
            self.posti_prenotati += num_posti
            return f"Posti prenotati: {num_posti}"
        else:
            return f"Mi dispiace, non ci sono abbastanza posti"
    
    def posti_disponibili (self) -> str:
        return f"Posti disponibili: {self.posti_totali - self.posti_prenotati}"

class Cinema:

    def __init__(self):
        self.sale:list = []

    def aggiungi_sala (self, sala: Sala):
        if sala not in self.sale:
            self.sale.append(sala)

    def prenota_film(self, titolo_film: str, num_posti: int) -> str:
        for sala in self.sale:
            if sala.film.titolo == titolo_film:
                return sala.prenota_posti(num_posti)
            else:
                return f"Sorry, {titolo_film} is not in program"



cinema = Cinema() #creo un cinema
film1 = Film("Interstellar", 250) # creo un film
sala1 = Sala(1, film1, 500) # creo una sala
cinema.aggiungi_sala(sala1) # aggiungo la sala al cinema
print(cinema.prenota_film("Interstellar", 5)) # prenoto biglietti i dati si aggiornano 
print(cinema.prenota_film("Interstellar", 150)) # prenoto i biglietti i dati si aggiornano
print(cinema.prenota_film("Interstellar", 410))