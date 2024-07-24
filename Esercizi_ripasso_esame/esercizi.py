#  Scrivi una funzione che somma tutti i numeri interi di una lista che sono maggiori di un dato valore intero definito threshold.

def sum_above_threshold(numbers: list[int], max_num: int) -> int:
    result: int = 0
    for x in numbers:
        if x > max_num:
            result += x
        else:
            continue
    
    return result

# Scrivi una funzione che prende una lista di numeri e ritorna un dizionario che classifica i numeri in liste separate per numeri pari e dispari.

def classifica_numeri(lista: int) -> dict[str:list[int]]:
    risultato: dict = {"pari": [], "dispari": []}
    for x in lista:
        if x % 2 == 1:
            risultato["dispari"].append(x)
        else:
            risultato["pari"].append(x)
    
    return risultato

# Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un nuovo dizionario con solo i prodotti 
# che hanno un prezzo superiore a 20, ma scontati del 10%.

def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    
    for k,v in prodotti.items():
        if v < 20.0:
           prodotti[k] = 0
        else:
            prodotti[k] = v -(v * 10)/100
    prodotti2 = prodotti.copy()
    for k,v in prodotti2.items():
        if v == 0:
            del prodotti[k]
    return prodotti

# Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
# a) 1, 2, 3, 4, 5, 6, 7
# b) 3, 8, 13, 18, 23
# c) 20, 14, 8, 2, -4, -10
# d) 19, 27, 35, 43, 51

def print_seq(): 
    
    print("Sequenza a):")
    for x in range(1,8, 1):
        print(x)
    print()    

    print("Sequenza b):")
    for x in range(3,24, 5):
        print(x)
    print()
    print("Sequenza c):")
    for x in range(20,-11, -6):    
        print(x)
    print()
    print("Sequenza d):")
    for x in range(19, 52, 8):
        print(x)
    print()
    
    return

# Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.

def frequency_dict(elements: list) -> dict:
    risultato: dict = {}
    for x in elements:
        if x not in risultato.keys():
            risultato[x] = 1
        else:
            risultato[x] += 1
    
    return risultato

# Scrivere il frammento di codice che cambi il valore intero memorizzato nella variabile x nel seguente modo:
# - se x è pari, deve essere diviso per 2;
# - se x è dispari deve essere moltiplicato per 3 e gli deve essere sottratto 1.

def transform(x: int) -> int:
    if x % 2 == 0:
        return (x / 2)
    else:
        return (x * 3 - 1)

# Scrivi una funzione che accetti tre parametri: username, password e status di attivazione dell'account 
# (attivo/non attivo). L'accesso è consentito solo se il nome utente è "admin", la password corrisponde a "12345" 
# e l'account è attivo. La funzione ritorna "Accesso consentito" oppure "Accesso negato".

def check_access(username: str, password: str, is_active: bool) -> str:
    if username == "admin" and password == "12345" and is_active == True:
        return "Accesso consentito"
    else:
        return "Accesso negato"

# Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se la chiave è già presente, 
# aggiungi il valore alla lista di valori già associata alla chiave.

def lista_a_dizionario(tuples:list[tuple]) -> dict[str:list[int]]:
    risultato = {}
    for x in tuples:
        k = x[0]
        v = x[1]
        if k not in risultato:
            risultato[k] = [v]
        else:
            risultato[k].append(v)
    return risultato

# Scrivi una funzione che prenda un dizionario e un valore, e ritorni la prima chiave che 
# corrisponde a quel valore, o None se il valore non è presente.

def trova_chiave_per_valore(dizionario: dict[str: int], valore: int) -> str:
    for k in dizionario.keys():
        if dizionario[k] == valore:
            return k
    
    return None

# Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    for k,v in dict2.items():
        if k in dict1:
            dict1[k] += v
        else:
            dict1[k] = v
    
    return dict1

# Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) è soddisfatta per procedere con un'operazione. 
# L'operazione può procedere solo se la condizione A è vera o se entrambe le condizioni B e C sono vere. La funzione deve ritornare 
# "Operazione permessa" oppure "Operazione negata" a seconda delle condizioni che sono soddisfatte.

def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    if conditionA == True or conditionB and conditionC == True:
        return "Operazione permessa"
    else:
        return "Operazione negata"
    
#  Progettare un sistema di gestione della biblioteca con i seguenti requisiti:

# Classe Book:

# Attributi:
# book_id: str - Identificatore di un libro.
# title: str - titolo del libro.
# author: str - autore del libro
# is_borrowed: boolean - booleano che indica se il libro è in prestito o meno.

# Metodi:
# borrow()-Contrassegna il libro come preso in prestito se non è già preso in prestito.
# return_book()- Contrassegna il libro come restituito.

class Book:
    def __init__(self, book_id: str, title: str, author:str) -> None:
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False
    
    def borrow_book(self):
        self.is_borrowed = True

    def return_book(self):
        self.is_borrowed = False

class Member:
    def __init__(self, member_id: str, name: str) -> None:
        self.member_id = member_id
        self.name = name
        self.borrowed_books:list = [] 

    def borrow_book(self, book: Book):
        self.borrowed_books.append(book.title)
    
    def return_book(self, book: Book):
        self.borrowed_books.remove(book.title)

class Library:
    def __init__ (self):
        self.books: dict[str, Book] = dict()
        self.members:  dict[str, Member] = dict()
    
    def add_book(self, book_id: str, title: str, author: str):
        book = Book(book_id, title, author)
        self.books[book_id] = book
    
    def register_member(self, member_id: str, name: str):
        member = Member(member_id, name)
        self.members[member_id] = member
    
    def borrow_book(self, member_id: str, book_id: str):
        if member_id in self.members:    
            if book_id in self.books:
                if self.books[book_id].is_borrowed != True:
                    self.books[book_id].borrow_book()
                    self.members[member_id].borrow_book(self.books[book_id])
                elif self.books[book_id].is_borrowed == True:
                    print("Book is already borrowed")
            else:
                print("Book not found")
        else:
            print("Member not found")

    def return_book (self, member_id: str, book_id: str):
        if member_id in self.members and book_id in self.books: 
            if self.books[book_id].title in self.members[member_id].borrowed_books:
                self.members[member_id].return_book(self.books[book_id])
                self.books[book_id].return_book()
            else:
                print("Book not borrowed by this member")
                #print(f" {self.books[book_id]} {self.members[member_id].borrowed_books}")
    
    def get_borrowed_books(self, member_id: str) -> list[Book]:
        return self.members[member_id].borrowed_books
    

# Progettare un semplice sistema bancario con i seguenti requisiti:

# Classe del Account:
# Attributi:
# account_id: str - identificatore univoco per l'account.
# balance: float - il saldo attuale del conto.
# Metodi:
# deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.
# get_balance(): restituisce il saldo corrente del conto.
# Classe Bank:
# Attributi:
# accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
# Metodi:
# create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
# deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
# get_balance(account_id): restituisce il saldo del conto con l'ID specificato.

class Account:
    def __init__(self, account_id: str, balance: float ):
        self.account_id = account_id
        self.balance = balance

    def deposit (self, amount: float ):
        self.balance += amount
    
    def get_balance(self) -> str:
        return self.balance
    
class Bank:
    def __init__(self):
        self.accounts: dict [str, Account] = {}
    
    def create_account(self, account_id: Account):
        if account_id not in self.accounts.keys():
            account: Account = Account(account_id, 0) 
            self.accounts[account_id] = account
            return account
        else:
            print("Account with this ID already exists") 

    def deposit(self, account_id: str, amount: float):
        self.accounts[account_id].deposit(amount)
    
    def get_balance(self, account_id):
        if account_id in self.accounts:
            return self.accounts[account_id].balance
        else:
            print("Account not found")

# Sviluppa un sistema per la gestione delle ricette in Python che permetta agli utenti di creare, modificare, e 
# cercare ricette basate sugli ingredienti. Il sistema dovrà essere capace di gestire una collezione (dizionario) 
# di ricette e i loro ingredienti.
# Classe:
# - RecipeManager:
#     Gestisce tutte le operazioni legate alle ricette.
#     Metodi:
#     - create_recipe(name, ingredients): Crea una nuova ricetta con il nome specificato e una lista di ingredienti. 
# Restituisce un nuovo dizionario con la sola ricetta appena creata o un messaggio di errore se la ricetta esiste già.
#     - add_ingredient(recipe_name, ingredient): Aggiunge un ingrediente alla ricetta specificata. Restituisce la ricetta 
# aggiornata o un messaggio di errore se l'ingrediente esiste già o la ricetta non esiste.
#     - remove_ingredient(recipe_name, ingredient): Rimuove un ingrediente dalla ricetta specificata. Restituisce la ricetta 
# aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.
#     - update_ingredient(recipe_name, old_ingredient, new_ingredient): Sostituisce un ingrediente con un altro nella 
# ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o 
# la ricetta non esiste.
#     - list_recipes(): Elenca tutte le ricette esistenti.
#     - list_ingredients(recipe_name): Mostra gli ingredienti di una specifica ricetta. Restituisce un elenco di ingredienti 
# o un messaggio di errore se la ricetta non esiste.
#     - search_recipe_by_ingredient(ingredient): Trova e restituisce tutte le ricette che contengono un determinato ingrediente. 
# Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente.

class RecipeManager:
    def __init__(self) -> None:
        self.recipe: dict[str, list[str]] = {}
    
    def create_recipe (self, name: str, ingredient: list[str]) -> dict:
        if name not in self.recipe:
            self.recipe[name] = ingredient
            return {name: self.recipe[name]}
        else:
            raise ValueError ("La ricetta esiste già")
    
    def add_ingredient (self, recipe_name: str, ingredient: list[str]) -> dict:
        if recipe_name in self.recipe:
                if ingredient in self.recipe[recipe_name]:
                    return f"{ingredient} è già presente nell'elenco"
                else:
                    self.recipe[recipe_name].append(ingredient)
                    return {recipe_name: self.recipe[recipe_name]}
        else:
            return f"{recipe_name} non è presente nell'elenco"
    
    def remove_ingredient (self, recipe_name: str, ingredient: str) -> dict:
        if recipe_name in self.recipe:
            if ingredient in self.recipe[recipe_name]:
                self.recipe[recipe_name].remove(ingredient)
                return {recipe_name: self.recipe[recipe_name]}
            elif ingredient not in self.recipe[recipe_name]:
                return f"{ingredient} non è presente"
        elif recipe_name not in self.recipe:
            return f"{recipe_name} non è presente nella lista"

    def update_ingredient (self, recipe_name: str, old_ingredient:str, new_ingredient: str) -> dict:
        if old_ingredient in self.recipe[recipe_name]:
            posizione = self.recipe[recipe_name].index(old_ingredient)
            self.recipe[recipe_name].remove(old_ingredient)
            self.recipe[recipe_name].insert(posizione, new_ingredient)
            return {recipe_name: self.recipe[recipe_name]}
        elif recipe_name not in self.recipe:
            return f"{recipe_name} non è presente nell'elenco"
        elif old_ingredient not in self.recipe[recipe_name]:
            return f"{old_ingredient} non è presente nella lista di ingredienti"
    
    def list_recipes (self) -> list:
        ricette: list = []
        for k in self.recipe.keys():
            ricette.append(k)
        return ricette

    def list_ingredients (self, recipe_name: str):
        if recipe_name in self.recipe:
            return self.recipe[recipe_name]
        elif recipe_name not in self.recipe:
            return f"{recipe_name} non è nell'elenco"

    def search_recipe_by_ingredient(self, ingredient) -> list:
        for k,v in self.recipe.items():
            if ingredient in v:
                return {k: self.recipe[k]}
            elif ingredient not in v:
                return f"Nessuna ricetta contiene {ingredient}"
            

# In questo esercizio, creeremo una gerarchia di classi per rappresentare diversi tipi di veicoli.
 
# 1. Classe Base: Veicolo
# Crea una classe base chiamata Veicolo con i seguenti attributi e metodi:
 
# Attributi:
# - marca (stringa)
# - modello (stringa)
# - anno (intero)

# Metodi:
# - __init__(self, marca, modello, anno): metodo costruttore che inizializza gli attributi marca, modello e anno.
# - descrivi_veicolo(self): metodo che stampa una descrizione del veicolo nel formato "Marca: [marca], Modello: [modello], Anno: [anno]".

# 2. Classe Derivata: Auto
# Crea una classe derivata chiamata Auto che eredita dalla classe Veicolo e aggiunge i seguenti attributi e metodi:
 
# Attributi:
# - numero_porte (intero)

# Metodi:
# - __init__(self, marca, modello, anno, numero_porte): metodo costruttore che inizializza gli attributi della classe base e numero_porte.
# - descrivi_veicolo(self): metodo che sovrascrive quello della classe base per includere anche il - numero di porte nella descrizione,
# nel formato "Marca: [marca], Modello: [modello], Anno: [anno], Numero di porte: [numero_porte]".

# 3. Classe Derivata: Moto
# Crea una classe derivata chiamata Moto che eredita dalla classe Veicolo e aggiunge i seguenti attributi e metodi:
 
# Attributi:
# - tipo (stringa, ad esempio "sportiva", "cruiser", ecc.)

# Metodi:
# - __init__(self, marca, modello, anno, tipo): metodo costruttore che inizializza gli attributi della classe base e tipo.
# - descrivi_veicolo(self): metodo che sovrascrive quello della classe base per includere anche il tipo di moto nella descrizione, 
# nel formato "Marca: [marca], Modello: [modello], Anno: [anno], Tipo: [tipo]".

class Veicolo:
    def __init__(self, marca: str, modello: str, anno: int) -> None:
        self.marca = marca
        self.modello = modello
        self.anno = anno        
    
    def descrivi_veicolo (self) -> str:
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}")


class Auto(Veicolo):
    def __init__(self, marca: str, modello: str, anno: int, numero_porte: int) -> None:
        super().__init__(marca, modello, anno)
        self.numero_porte = numero_porte
    
    def descrivi_veicolo(self) -> str:
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Numero di porte: {self.numero_porte}")


class Moto(Veicolo):
    def __init__(self, marca: str, modello: str, anno: int, tipo: str) -> None:
        super().__init__(marca, modello, anno)
        self.tipo = tipo

    def descrivi_veicolo(self) -> str:
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Tipo: {self.tipo}")