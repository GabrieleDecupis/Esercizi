# Testi Digitali

# Si definisca una classe Documento che contenga una variabile di tipo stringa chiamata testo e che memorizza qualsiasi 
# contenuto testuale per il documento.
# Si crei un metodo getText() che restituisca il testo. Si crei un metodo setText() per impostare il testo. 
# Scrivere un metodo isInText() che restituisce True se un documento contiene la parola chiave specificata.

# Si definisca poi una classe Email che sia derivata da Documento e che includa le variabili per il mittente, il 
# destinatario e il titolo del messaggio.
# Si implementino i metodi get() e set() appropriati per tali variabili. Il corpo del messaggio dell’e-mail dovrebbe 
# essere memorizzato nella variabile ereditata testo.
# Si ridefinisca il metodo getText() per concatenare e ritornare tutti i campi di testo (mittente, destinatario, 
# titolo del messaggio, e messaggio) come di seguito:
 
# Da: alice@example.com, A: bob@example.com
# Titolo: Incontro
# Messaggio: Ciao Bob, possiamo incontrarci domani
 
# Inoltre, si implementi un metodo writeToFile() per scrivere il risultato del metodo getText() in un file di testo e in 
# un percorso specificato.
 
# Analogamente, si definisca una classe File che sia derivata da Documento e includa una variabile per il nomePercorso.
# Crea un file document.txt con all'interno la stringa "Questo e' il contenuto del file." e salvalo in una directory a tua scelta 
# e che sarà indicata in nomePercorso.
# I contenuti testuali del file dovrebbero essere letti da questo file di testo al percorso specificato in nomePercorso e 
# memorizzati nella variabile ereditata testo tramite un metodo leggiTestoDaFile().
# Si ridefinisca il metodo getText() che concateni e ritorni il nome del percorso e il testo, come di seguito:
 
# Percorso: nomePercorso/document.txt
# Contenuto: Questo e' il contenuto del file.

class Document:
    def __init__(self, testo: str) -> None:
        self.testo = testo
    
    def get_text(self) -> str:
        return self.testo
    
    def set_text(self, testo_nuovo: str) -> None:
        self.testo = testo_nuovo 
    
    def isintext(self, k_word: str) -> bool:
        if k_word in self.testo:
            return True
        else:
            return False
    
class Email(Document):
    def __init__(self, mittente: str, destinatario: str, titolo_messsaggio: str, testo: str = None ) -> None:
        super().__init__(testo)
        self.mittente = mittente
        self.destinatario = destinatario
        self.titolo_messaggio = titolo_messsaggio 

    def get_mittente(self)-> str:
        return self.mittente

    def get_destinatario(self)-> str:
        return self.destinatario    

    def get_titolo_messaggio(self)-> str:
        return self.titolo_messaggio
    
    def set_mittente(self, new_mittente:str) -> None:
        self.mittente = new_mittente
    
    def set_destinatario(self, new_destinatario: str)-> None:
        self.destinatario = new_destinatario

    def set_titolo(self, new_titolo: str) -> None:
        self.titolo_messaggio = new_titolo

    def get_text(self) -> str:
        return f"Da: {self.mittente}, A: {self.destinatario} \n Titolo: {self.titolo_messaggio} \n Messaggio: {self.testo}"









email1 = Email("io", "tu", "egli", "ciao")
print(email1.get_text())
