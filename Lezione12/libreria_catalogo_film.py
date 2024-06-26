# Sistema Avanzato di Gestione Biblioteca
# 
# Si desidera sviluppare un sistema per la gestione di una biblioteca in Python. Il sistema deve permettere di gestire un 
# inventario di libri e le operazioni di prestito e restituzione degli stessi. Gli utenti del sistema devono essere in grado di aggiungere 
# libri al catalogo, prestarli, restituirli e visualizzare quali libri sono disponibili in un dato momento.
# 
# Classi:
# 
# - Libro: Rappresenta un libro con titolo, autore, stao del prestito. Il libro deve essere inizialmente disponibile (non prestato).
# 
# - Biblioteca: Gestice tutte le operazioni legate alla gestione di una biblioteca.
# 
# Metodi:
#     - aggiungi_libro(libro): Aggiunge un nuovo libro al catalogo della biblioteca. Restituisce un messaggio di conferma.
# 
#     - presta_libro(titolo): Cerca un libro per titolo e, se disponibile e non già prestato, lo segna come disponibile. 
#       Restituisce un messaggio di stato.
# 
#     - restituisci_libro(titolo): Cerca un libro per titolo e, se trovato e prestato, lo segna come disponibile. Restituisce un messaggio di stato.
# 
#     - mostra_libri_disponibili(): Restituisce una lista dei titoli dei libri attualmente disponibili. 
#       Se non ci sono libri disponibili, restituisce un messaggio di errore.
# 
# Test Cases:
# - Un amministratore della biblioteca aggiunge alcuni libri all'inventario.
# 
# - Un utente prende in prestito un libro, che viene quindi marcato come non disponibile.
# 
# - L'utente restituisce il libro, che viene marcato di nuovo come disponibile.
# 
# - In qualsiasi momento, un utente può visualizzare quali libri sono disponibili per il prestito.

class Libro:
    def __init__(self, titolo: str, autore: str) -> None:
        self.titolo = titolo
        self.autore = autore
        self.stato_del_prestito = False

class Biblioteca:
    def __init__(self) -> None:
        self.libri: list[Libro] = []
    
    def aggiungi_libro(self, libro: Libro):
        if libro not in self.libri:
            self.libri.append(libro)
        else: 
            return f"Il libro {libro.titolo} è stato già aggiunto alla biblioteca"
    
    def presta_libro(self, titolo:str):
        for libro_da_prestare in self.libri:
            if titolo == libro_da_prestare.titolo:
                if libro_da_prestare.stato_del_prestito == False:
                    libro_da_prestare.stato_del_prestito = True
                    return f"Hai appena noleggiato {titolo}"
                else:
                    return f"Il libro {titolo} non è disponibile al momento"
            else:
                return f"il libro {titolo} non è presente nella biblioteca"
    
    def restituisci_libro(self, titolo: str):
        for libro_da_prestare in self.libri:
            if titolo == libro_da_prestare.titolo and libro_da_prestare.stato_del_prestito == True:
                libro_da_prestare.stato_del_prestito = False
                return f"Hai appena restituito {titolo}"

    def mostra_libri_disponibili(self):
        lista_libri_disponibili = []
        for libro in self.libri:
            if libro.stato_del_prestito == False:
                lista_libri_disponibili.append(libro.titolo)
                if lista_libri_disponibili == []:
                    return f"Non è disponibile nessun libro per il noleggio"
        return f"Libri disponibili {', '.join(titolo for titolo in lista_libri_disponibili)}"
            
    

# libro1 = Libro("eragon", "ciccio sprizzo")
# libro2 = Libro("topolino", "pippo")
# biblioteca1 = Biblioteca()
# biblioteca1.aggiungi_libro(libro1)
# biblioteca1.aggiungi_libro(libro2)
# print(biblioteca1.presta_libro("eragon"))
# print(biblioteca1.mostra_libri_disponibili())
# print(biblioteca1.restituisci_libro("eragon"))
# print(biblioteca1.mostra_libri_disponibili())
# print(biblioteca1.presta_libro("topolina"))


# Catalogo Film 

# Sviluppa un sistema in Python per la gestione di un catalogo film che permetta di aggiungere, rimuovere e cercare film 
# di un particolare regista. Il sistema dovrebbe consentire anche di visualizzare tutti i registi e i loro film.

# Classe:
# - MovieCatalog(): Gestisce tutte le operazioni legate al catalogo dei film.

#     Metodi:
#     - add_movie(director_name, movies): Aggiunge uno o più film a un regista specifico nel catalogo. Se il regista non esiste, 
#       viene creato un nuovo record. Se il regista esiste, la sua lista di film viene aggiornata.

#     - remove_movie(director_name, movie_name): Rimuove un film specifico dall'elenco dei film di un regista. 
#       Se tutti i film sono rimossi, il regista può essere opzionalmente rimosso dal catalogo.

#     - list_directors(): Elenca tutti i registi presenti nel catalogo.

#     - get_movies_by_director(director_name): Restituisce tutti i film di un regista specifico.

#     - search_movies_by_title(title): Trova tutti i film che contengono una certa parola nel titolo. Restituisce un elenco dei registi 
#       e dei rispettivi film che contengono la parola cercata o un messaggio di errore se nessun film contiene la parola cercata nel titolo.

class MovieCatalog:
    def __init__(self) -> None:
        self.catalogo: dict = {}
    
    def add_movie(self, director_name: str, movies: list[str]):
        if director_name not in self.catalogo:
            self.catalogo[director_name] = movies
        else:
            for movie in movies:
                self.catalogo[director_name].append(movie)
    
    def remove_movie(self, director_name: str, movie: str):
        if director_name in self.catalogo:
            if movie in self.catalogo[director_name]:
                self.catalogo[director_name].remove(movie)
            else:
                print(f"Non è stato possibile rimuovere il film {movie} in quanto non è presente nell'elenco del regista {director_name}")
            if self.catalogo[director_name] == []:
                x = input(f"Il regista {director_name} non ha più film nell'elenco, vuoi rimuoverlo? Y/N: ")
                if x == "Y":
                    del self.catalogo[director_name]
        else:
            print(f"Il regista {director_name} non è presente nel catalogo")
        
    def list_directors(self) -> str:
        registi: list = []
        for regista in self.catalogo.keys():
            registi.append(regista)
        return f"Registi disponibili: {', '.join(registi)}"

    def get_movies_by_director(self, director_name) -> str:
        if director_name in self.catalogo:
            films: list = []
            for film in self.catalogo[director_name]:
                films.append(film)
            if films == []:
                return f"Il regista {director_name} è presente nel catalogo ma non ci sono film a lui assegnati!"
            return f"I film del regista {director_name} sono: {', '.join(films)}"
        else:
            return f"Il regista {director_name} non è presente nell'elenco"
    
    def search_movies_by_title(self, title: str) -> list[str]:
        result: list = []
        title = title.lower()
        for regista in self.catalogo:
            films: list[str] = self.catalogo[regista]
            for film in films:
                if title in film:
                    if regista not in result:
                        result.append(regista)
                    result.append(film)
        if result:
            return result
        return f"Non è stato trovato nessun film con il titolo: {title} "


# catalogo1 = MovieCatalog()
# catalogo1.add_movie("ciccio", ["1", "2", "3"])
# catalogo1.add_movie("ciccia", ["1", "23", "4", "5","3"])
# catalogo1.remove_movie("ciccio", "1")
# catalogo1.remove_movie("ciccio", "2")
# catalogo1.remove_movie("ciccio", "3")
# print(catalogo1.catalogo)
# print(catalogo1.list_directors())
# print(catalogo1.get_movies_by_director("ciccio"))
# print(catalogo1.search_movies_by_title("2"))
