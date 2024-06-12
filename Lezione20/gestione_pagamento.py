# Si definisca una nuova classe Pagamento che contiene un attributo privato e di tipo float che memorizza l'importo 
# del pagamento e si definiscano appropriati metodi get() e set(). L'importo non è un parametro da passare in input alla classe 
# Pagamento ma deve essere inizializzato utilizzando il metodo set() dove opportuno. Si crei inoltre un metodo dettagliPagamento() 
# che visualizza una frase che descrive l'importo del pagamento, ad esempio: "Importo del pagamento: €20.00". Quando viene stampato, 
# l'importo è sempre con 2 cifre decimali.

# Successivamente, si definisca una classe PagamentoContanti che sia derivata da Pagamento e definisca l'importo. 
# Questa classe dovrebbe ridefinire il metodo dettagliPagamento() per indicare che il pagamento è in contanti. 
# Si definisca inoltre il metodo inPezziDa() che stampa a schermo quante banconote da 500 euro, 200 euro, 100 euro, 
# 50 euro, 20 euro, 10 euro, 5 euro e/o in quante monete da 2 euro, 1 euro, 0,50 euro, 0,20 euro, 0,10 euro, 0,05 euro, 
# 0,01 euro sono necessarie per pagare l'importo in contanti.

# Si definisca una classe PagamentoCartaDiCredito derivata anch'essa da Pagamento e che definisce l'importo. 
# Questa classe deve contenere gli attributi per il nome del titolare della carta, la data di scadenza, e il numero della carta di credito. 
# Infine, si ridefinisca il metodo dettagliPagamento() per includere tutte le informazioni della carta di credito oltre 
# all'importo del pagamento.

# Per il test, si creino almeno due oggetti di tipo PagamentoContanti e due di tipo PagamentoCartaDiCredito con valori differenti 
# e si invochi dettagliPagamento() per ognuno di essi.

# Esempio di output:
# Pagamento in contanti di: €150.00
# 150.00 euro da pagare in contanti con:
# 1 banconota da 100 euro
# 1 banconota da 50 euro

# Pagamento in contanti di: €95.25
# 95.25 euro da pagare in contanti con:
# 1 banconota da 50 euro
# 2 banconote da 20 euro
# 1 banconota da 5 euro
# 1 moneta da 0.2 euro
# 1 moneta da 0.05 euro

# Pagamento di: €200.00 effettuato con la carta di credito
# Nome sulla carta: Mario Rossi
# Data di scadenza: 12/24
# Numero della carta: 1234567890123456

# Pagamento di: €500.00 effettuato con la carta di credito
# Nome sulla carta: Luigi Bianchi
# Data di scadenza: 01/25
# Numero della carta: 6543210987654321

class Pagamento:
    def __init__(self) -> None:
        self.__import: float = None
    
    def get_pagamento(self) -> float:
        return self.__import
    
    def set_pagamento(self, new_import: float):
        self.__import = new_import

    def dettagliPagamento(self) -> str:
        return f"Importo del pagamento: {self.get_pagamento():.2f}"

class PagamentoContanti(Pagamento):
    def __init__(self, importo: float) -> None:
        super().__init__()
        self.set_pagamento(importo)

    def dettagliPagamento(self) -> str:
        return f"Pagamento in contanti: {self.get_pagamento():.2f}"

    def inPezziDa(self):
        euro: dict = {500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.5: 0, 0.2: 0, 0.1: 0, 0.05: 0, 0.01: 0}
        contanti = self.get_pagamento()
        while contanti >= 0:
            for x in euro.keys():
                if contanti - x >= 0:
                    euro[x] += 1
                else:
                    continue
                break
            contanti -= x
            contanti = round(contanti, 2)
                
        for k,v in euro.items():
            if v > 1 and k > 2:
                print(f"{v} banconote da {k} euro")
            elif v == 1 and k > 2:
                print(f"{v} banconota da {k} euro")
            elif v > 1 and k <= 2:
                print(f"{v} monete da {k} euro")
            elif v == 1 and k <= 2:
                print(f"{v} moneta da {k} euro")

class PagamentoCartaDiCredito(Pagamento):
    def __init__(self, importo: float, nome_sulla_carta: str, data_scadenza: str, numero_carta: str) -> None:
        super().__init__()
        self.set_pagamento(importo)
        self.nome_sulla_carta = nome_sulla_carta
        self.data_scadenza = data_scadenza
        self.numero_carta = numero_carta
    
    def dettagliPagamento(self) -> str:
        #return f"Pagamento di: {self.get_pagamento():.2f} effettuato con la carta di credito\n"+f"Nome sulla carta: {self.nome_sulla_carta}\n"+f"Data di scadenza: {self.data_scadenza}\n"+f"Numero della carta: {self.numero_carta}"
        print(f"Pagamento di: {self.get_pagamento():.2f} effettuato con la carta di credito\n"
              f"Nome sulla carta: {self.nome_sulla_carta}\n"
              f"Data di scadenza: {self.data_scadenza}\n"
              f"Numero della carta: {self.numero_carta}")

