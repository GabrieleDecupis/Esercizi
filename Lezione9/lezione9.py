# esercizio 1
#
# Progettare un semplice sistema bancario con i seguenti requisiti:
# 
#     Classe del Account:
#         Attributi:
#             account_id: str - identificatore univoco per l'account.
#             balance: float - il saldo attuale del conto.
#         Metodi:
#             deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.
#             get_balance(): restituisce il saldo corrente del conto.
#     Classe Bank:
#         Attributi:
#             accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
#         Metodi:
#             create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
#             deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
#             get_balance(account_id): restituisce il saldo del conto con l'ID specificato.

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


# esercizio 2
#
# Data una lista di interi, chiamata tree, che rappresenta un albero binario, restituire True se l'albero è simmetrico; False altrimenti.
# 
# La lista di interi è formata così:
# 
#     L'elemento in posizione 0 corrisponde alla radice
#     Dato un nodo in posizione i, il suo figlio sinistro si trova in posizione 2*i + 1
#     Dato un nodo in posizione i, il suo figlio destro si trova in posizione 2*(i+1)
#     Se, dato un indice i si va fuori bound facendo almeno uno dei calcoli dei punti precedenti, significa che il nodo che corrisponde 
#     a quell'indice è una foglia.

class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def symmetric(tree: list[int]) -> bool:
    if tree[1] != tree[2]:
        return False
    else:
        if tree[3] == tree[6] and tree[4] == tree[5]:
            return True
        else:
            return False
        

# esercizio 3
#
# Determina se una tavola Sudoku 9 x 9 è valida. Solo le celle compilate devono essere convalidate secondo le seguenti regole:
# 
#     Ogni riga deve contenere le cifre 1-9 senza ripetizioni.
#     Ciascuna colonna deve contenere le cifre da 1 a 9 senza ripetizioni.
#     Ciascuno dei nove sottoriquadri 3 x 3 della griglia deve contenere le cifre 1-9 senza ripetizione.
# 
# Nota:
# 
#     Una tavola Sudoku (parzialmente riempita) potrebbe essere valida ma non è necessariamente risolvibile.
#     Solo le celle riempite devono essere convalidate secondo le regole menzionate.
# 

# def valid_sudoku(board: list[list[str]]) -> bool:
#     for x in board:
#         for y in x:
#             if 
        


# esercizio 4
#
# Progettare un sistema di gestione della biblioteca con i seguenti requisiti:
# 
#     Classe Book:
#         Attributi:
#             book_id: str - Identificatore di un libro.
#             title: str - titolo del libro.
#             author: str - autore del libro
#             is_borrowed: boolean - booleano che indica se il libro è in prestito o meno.
#         Metodi:
#             borrow()-Contrassegna il libro come preso in prestito se non è già preso in prestito.
#             return_book()- Contrassegna il libro come restituito.


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
        

#     Classe Member:
#         Attributi:
#             member_id: str - identificativo del membro.
#             name: str - il nome del membro.
#             borrowed_books: list[Book] - lista dei libri presi in prestito.
#         Metodi:
#             borrow_book(book): aggiunge il libro nella lista borrowed_books se non è già stato preso in prestito.
#             return_book(book): rimuove il libro dalla lista borrowed_books.

class Member:
    def __init__(self, member_id: str, name: str) -> None:
        self.member_id = member_id
        self.name = name
        self.borrowed_books:list = [] 

    def borrow_book(self, book: Book):
        self.borrowed_books.append(book.title)
    
    def return_book(self, book: Book):
        self.borrowed_books.remove(book)

#     Classe Library:
#         Attributi:
#             books: dict[str, Book] - dizionario che ha per chiave l'id del libro e per valore l'oggetto Book
#             members: dict[str, Member] - dizionario che ha per chiave l'id del membro e per valore l'oggetto Membro
#         Metodi:
#             add_book(book_id: str, title: str, author: str): Aggiunge un nuovo libro nella biblioteca.
#             register_member(member_id:str, name: str): Iscrive un nuovo membro nella biblioteca.
#             borrow_book(member_id: str, book_id: str): Permette al membro di prendere in prestito il libro.
#             return_book(member_id: str, book_id: str): Permette al membro di restituire il libro.
#             get_borrowed_books(member_id): list[Book] - restituisce la lista dei libri presi in prestito dal membro.
        
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
                else:
                    return "Book is already borrowed"
            else:
                return "Book not found"
        else:
            return "Member not found"

    def return_book (self, member_id: str, book_id: str):
        if member_id in self.members and book_id in self.books:
            self.members[member_id].return_book(self.books[book_id])
        else:
            return "Book not borrowed by this member"
    
    def get_borrowed_books(self, member_id: str) -> list[Book]:
        return self.members[member_id].borrowed_books


# esercizio 6:

# Data una stringa s e una lista di stringhe wordDict, restituisce True se s può essere segmentato in una sequenza separata 
# da spazi di una o più parole del dizionario; False altrimenti.

# Tieni presente che la stessa parola nel dizionario può essere riutilizzata più volte nella segmentazione.

# For example:

# print(word_break("leetcode",["leet","code"]))     True

# print(word_break("applepenapple", ["apple","pen"]))   True

# print(word_break("catsandog",["cats","dog","sand","and","cat"]))  False

def word_break(s: str, wordDict: list[str]) -> bool:
    count = 0
    parola_nella_lista = 0
    while parola_nella_lista <= len(wordDict) - 1:
        x = s[:count]
        if wordDict[parola_nella_lista] == x:
            s = s[count:]
            count = 0
            del wordDict[parola_nella_lista]
        else:
            count += 1
            if count > len(s):
                count = 0
                parola_nella_lista += 1
    if wordDict == []:
        return True
    else:
        return False


# esercizio 7

# Date due stringhe s e t, restituire True se t è un anagramma di s, e False altrimenti.

# Un anagramma è una parola o una frase formata riorganizzando le lettere di una parola o frase diversa, in genere 
# utilizzando tutte le lettere originali esattamente una volta.

# For example:

# print(anagram("anagram","nagaram")) True

def anagram(s: str, t: str) -> bool:
    if len(s) == len(t):
        lista_vuota = []
        lista_vuota2 = []
        for lettera in s:
            lista_vuota2.append(lettera)
        for lettera in t:
            if lettera in lista_vuota2:
                lista_vuota.append(lettera)
                lista_vuota2.remove(lettera)
        if len(lista_vuota) == len(s):
            return True
        else:
            return False
    else:
        return False

print(anagram("anagram","anargame")) 