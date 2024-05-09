class Person:
    # il costruttore si crea così:
    def __init__(self, name: str, surname: str, ssn: str) -> None:
        
        '''
        
        '''
        
        # name, surname, ssn sono tutti attributi della classe person
        self._name: str = name
        self._surname: str = surname
        self._ssn: str = ssn
        # self.attributi (self.name ecc) serve per memorizzare le valori nell'istanza ( person_1)
        # scrivendo self._name blocco eventuali modifiche nelle istanze
    def get_name(self):
        
        '''
        This function returns a person's name
        input: none
        return: self._name: str, the function returns the person's name
        '''
        
        return self._name

    def set_name(self, name: str) -> None:
        
        '''
        This function sett the attribute name
        input: name : str, the parameter contains the user's name
        return; None
        '''
        
        raise Exception("You cannot modify the name!!")
    # get serve per visualizzare i valori all'interno delle istanza solo se gli attributi hanno _ , set invece serve per modificare i valori
    # raise mi permette di bloccare un'eventuale modifica
    def get_ssn(self) -> str:
        '''
        This function returns a ssn value
        input: none
        return: self._ssn: str, the function returns ssn value
        '''
        
        return self._ssn

    def set_ssn(self, ssn: str) -> None:

        '''
        This function set the ssn
        input: ssn : str, the parameter contains the user's snn
        return: None
        '''

        self._ssn = ssn



person_1: Person = Person(name ="Gabriele", surname="De Cupis", ssn="DCPGRL97E28H501L")
person_2: Person = Person(name ="Valentino", surname="Rossi", ssn="VLKJHDSNJOSDNO")

queue: list[Person] = [person_1, person_2]
for person in queue:
    print(person.get_ssn())
    print(person.get_name())