# # esercizio 1

# Vogliamo gestire un contatore che può essere incrementato, decrementato, resettato e visualizzato. 
# La classe offre un modo semplice per tenere traccia di un conteggio che non può diventare negativo.

# Classe Contatore

#     Attributi:
#         - conteggio: un intero che conserva il valore del conteggio, inizializzato a 0.

#     Metodi:
#         - __init__(): Inizializza l'attributo conteggio a 0.
#         - setZero(): Imposta il conteggio a 0.
#         - add1(): Incrementa il conteggio di 1.
#         - sub1(): Decrementa il conteggio di 1, ma non permette che il conteggio diventi negativo. 
#           Se il conteggio è già 0, stampa un messaggio di errore.
#         - get(): Restituisce il valore corrente del conteggio.
#         - mostra(): Stampa a schermo il valore corrente del conteggio.

class Contatore:
    def __init__(self) -> None:
        self.contatore = 0

    def setZero(self) -> None:
        self.contatore = 0
    
    def add1(self) -> None:
        self.contatore += 1
    
    def sub1(self) -> None:
        if self.contatore > 0:
            self.contatore -= 1
        else:
            print("Non è possibile eseguire la sottrazione")
    
    def get(self):
        return self.contatore

    def mostra(self) -> str:
        print(f"Conteggio attuale: {self.contatore}")


# esercizio 2

# Sviluppa un sistema per la gestione delle ricette in Python che permetta agli utenti di creare, modificare, e cercare 
# ricette basate sugli ingredienti. Il sistema dovrà essere capace di gestire una collezione di ricette e i loro ingredienti.

# Classe:
# - RecipeManager:
#     Gestisce tutte le operazioni legate alle ricette.

#     Metodi:
#     - create_recipe(name, ingredients): Crea una nuova ricetta con il nome specificato e una lista di ingredienti. 
#       Restituisce un dizionario con la ricetta appena creata o un messaggio di errore se la ricetta esiste già.

#     - add_ingredient(recipe_name, ingredient): Aggiunge un ingrediente alla ricetta specificata. Restituisce la ricetta 
#       aggiornata o un messaggio di errore se l'ingrediente esiste già o la ricetta non esiste.

#     - remove_ingredient(recipe_name, ingredient): Rimuove un ingrediente dalla ricetta specificata. 
#       Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.

#     - update_ingredient(recipe_name, old_ingredient, new_ingredient): Sostituisce un ingrediente con un altro nella ricetta specificata. 
#       Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.

#     - list_recipes(): Elenca tutte le ricette esistenti.

#     - list_ingredients(recipe_name): Mostra gli ingredienti di una specifica ricetta. Restituisce un elenco di ingredienti o 
#       un messaggio di errore se la ricetta non esiste.

#     - search_recipe_by_ingredient(ingredient): Trova e restituisce tutte le ricette che contengono un determinato ingrediente. 
#       Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente.

