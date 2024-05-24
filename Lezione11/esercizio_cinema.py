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

    def __init__(self, film_name: str, film_duration: int) -> None:
        self.film_name = film_name
        self.film_duration = film_duration

class Sala:

    def __init__(self, id_number: int, film_in_program: str, tot_seats: int, seats_booked: int ) -> None:
        self.id_number = id_number
        self.film_in_program = film_in_program
        self.tot_seats = tot_seats
        self.seats_booked = seats_booked
    
    def prenota_posti (self, num_posti: int) -> int:
        if self.tot_seats - self.seats_booked >= num_posti:
            print(f"You just booked {num_posti} seats")
        else:
            print(f"Sorry, but there aren't enough seats. Attually we have available {self.tot_seats - self.seats_booked} seats")
    
    def posti_disponibili (self) -> str:
        print(f"Seats available: {self.tot_seats - self.seats_booked}")


class Cinema:

    def __init__(self, sale_cinema: list = []) -> None:
        self.sale_cinema: list[Sala] = sale_cinema

    def aggiungi_sala (self, sala: int):
        if sala not in self.sale_cinema:
            self.sale_cinema.append(sala)

    def prenota_film(self, film_name: str, num_posti: int):
        for x in self.sale_cinema:
            if film_name in x.film_in_program:
                if (x.tot_seats - x.seats_booked) >= num_posti:
                    print(f"You just booked {num_posti} seats for {film_name}")
                    break
                else:
                    print(f"Sorry, but there aren't enough seats for {film_name}. Attually we have available {x.tot_seats - x.seats_booked} seats")
                    break
            else:
                print(f"Sorry, {film_name} is not in program")
                break



sala1 = Sala(1, "Il pianeta del tesoro", 150, 15)
sala2 = Sala(2, "Interstelar", 150, 10)
sala3 = Sala(3, "Matrix", 200, 45)

cinema1 = Cinema([sala1, sala2, sala3])
cinema1.prenota_film("Il pianeta del tesoro", 155)
