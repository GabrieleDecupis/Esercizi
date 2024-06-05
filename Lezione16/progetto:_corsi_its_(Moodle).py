# In questo progetto, dovrai scrivere il codice per un sistema di gestione e creazione dei corsi ITS.
# Il sistema gestisce aule ed edifici (Parte 1), persone -studenti e docenti- in gruppi di studio (parte 2), e corsi (parte 3).
 
# ### Classe Room:
# La classe Room rappresenta un'aula. Ogni aula ha un ID (id), un piano (floor), un numero di posti (seats) e un'area (area).
# L'area è calcolata come il doppio dei posti.

# - Metodi:
#     - get_id(): Restituisce l'ID dell'aula.
#     - get_floor(): Restituisce il piano dell'aula.
#     - get_seats(): Restituisce il numero di posti dell'aula.
#     - get_area(): Restituisce l'area dell'aula.

# ### Classe Building:
# La classe Building rappresenta un edificio. Ogni edificio ha un nome (name), un indirizzo (address), un intervallo
# di piani (floors), e una lista di aule (rooms).

# - Metodi:
#     - get_floors(): Restituisce l'intervallo di piani dell'edificio.
#     - get_rooms(): Restituisce la lista delle aule nell'edificio.
#     - add_room(room): Aggiunge un'aula all'edificio, solo se il piano dell'aula è compreso nell'intervallo di piani dell'edificio.
#     - area(): Restituisce l'area totale dell'edificio sommando le aree di tutte le aule.

class Room:
    def __init__(self, id: str, floor: int, seats: int) -> None:
        self.id = id
        self.floor = floor
        self.seats = seats
    
    def get_id(self) -> str:
        return self.id
    
    def get_floor(self) -> int:
        return self.floor
    
    def get_seats(self) -> int:
        return self.seats
    
    def get_area(self) -> int:
        return self.seats * 2

class Building:
    def __init__(self, name: str, address: str, floors: int):
        self.rooms: list[Room] = []
        self.name = name
        self.address = address
        self.floors = floors
    
    def get_floors(self) -> int:
        return self.floors
    
    def get_rooms(self) -> list:
        return self.rooms

    def add_room(self, room: Room) -> None:
        if min(self.floors) <= room.floor <= max(self.floors) :
            if room not in self.rooms:
                self.rooms.append(room)

    def area(self):
        area = 0
        for room in self.rooms:
            area += room.get_area()
        
        return area


	
# ### Classi Person, Student e Lecturer:
# La classe Person rappresenta una persona con un codice fiscale (cf), un nome (name), un cognome (surname), un'età (age).
# Le classi Student e Lecturer ereditano da Person.
# Uno studente è associato ad un gruppo di studio (group). Quindi, la classe Student ha il seguente metodo:
#     - set_group(group): Associa un gruppo di studio allo studente

# ### Classe Group:
# La classe Group rappresenta un gruppo di studio. Ogni gruppo ha un nome (name), un limite di studenti (limit), 
# una lista di studenti (students) e una lista di docenti (lecturers).
# - Metodi:
#     - get_name(): Restituisce il nome del gruppo
#     - get_limit(): Restituisce il limite di studenti nel gruppo
#     - get_students(): Resituisce la lista di studenti nel gruppo
#     - get_limit_lecturers(): Restituisce il limite di docenti nel gruppo. E' consentito 1 docente ogni 10 studenti. 
#       Il gruppo può avere almeno 1 docente, anche se ci sono meno di 10 studenti.
#     - add_student(student): Aggiunge uno studente al gruppo, solo se il limite per gli studenti non è stato raggiunto.
#     - add_lecturer(lecturer): Aggiunge un docente al gruppo, solo se il limite per i docenti non è stato raggiunto.

class Person:
    def __init__ (self,  cf: str, name: str, surname: str, age: int):
        self.cf = cf
        self.name = name
        self.surname = surname
        self.age = age
        self.group = None

class Student(Person):
    def __init__(self, cf: str, name: str, surname: str, age: int):
        super().__init__(cf, name, surname, age)
    
    def set_group(self, group):
        self.group = group

class Lecturer(Person):
    def __init__(self, cf: str, name: str, surname: str, age: int):
        super().__init__(cf, name, surname, age)
    
class Group:
    def __init__(self, name: str, limit: int) -> None:
        self.students: list[Student] = []
        self.lecturers: list[Lecturer] = []
        self.name = name
        self.limit = limit
    
    def get_name(self) -> str:
        return self.name

    def get_limit(self) -> int:
        return self.limit
    
    def get_students(self) -> list:
        return self.students
    
    def get_limit_lecturers(self) -> int:
        num_student = len(self.students)
        num_prof = num_student // 10 + 1
        return num_prof
    
    def add_student(self, student: Student):
        if len(self.students) < self.limit:
            if student not in self.students:
                self.students.append(student)



    def add_lecturer(self, lecturer: Lecturer):
        if len(self.lecturers) < self.get_limit_lecturers():
            if lecturer not in self.lecturers:
                self.lecturers.append(lecturer)

    

# ### Classe Course:
# La classe Course rappresenta un corso accademico. Ogni corso ha un nome (name) e una lista di gruppi (groups).
# - Metodi:
#     - register(student): Registra uno studente nel primo gruppo disponibile che non ha ancora raggiunto il limite di studenti.
#     - get_groups(): Restituisce la lista dei gruppi nel corso.
#     - add_group(group): Aggiunge un gruppo al corso.

class Course:
    def __init__(self, name: str) -> None:
        self.name = name
        self.groups: list[Group] = []
    
    def register(self, student: Student):
        for group in self.groups:
            if len(group.students) < group.limit:
                group.add_student(student)
                break
            
            
            
            
    
    def get_groups(self):
        return self.groups

    def add_group(self, group: Group):
        if group not in self.groups:
            self.groups.append(group)


# Creazione degli edifici
smi = Building(name="SMI", address="Via Sierra Nevada 60", floors=(-2, 3))
armellini = Building(name="ITIS", address="Basilica San Paolo", floors=(0, 4))

# Aggiunta delle stanze all'edificio smi
smi.add_room(Room(id="123", floor=3, seats=32))
smi.add_room(Room(id="333", floor=0, seats=42))
smi.add_room(Room(id="111", floor=6, seats=32))  # Questa stanza non viene aggiunta perché è fuori dal range dei piani
smi.add_room(Room(id="111", floor=-1, seats=32))

# Aggiunta delle stanze all'edificio smi
armellini.add_room(Room(id="567", floor=3, seats=22))
armellini.add_room(Room(id="888", floor=0, seats=32))
armellini.add_room(Room(id="999", floor=6, seats=22))  # Questa stanza non viene aggiunta perché è fuori dal range dei piani
armellini.add_room(Room(id="999", floor=2, seats=22))

# Output dei risultati
print("### SMI ###")
print(f"Stanze nell'edificio SMI: {[room.get_id() for room in smi.get_rooms()]}")
print(f"Area totale dell'edificio SMI: {smi.area()} m²")
print("### ARMELLINI ###")
print(f"Stanze nell'edificio ITIS: {[room.get_id() for room in armellini.get_rooms()]}")
print(f"Area totale dell'edificio ITIS: {armellini.area()} m²")


# Creazione dei gruppi
fullstack = Group(name="Fullstack", limit=1)
cloud = Group(name="Cloud", limit=10)
cyber = Group(name="Cyber", limit=10)

# Creazione di un corso e aggiunta dei gruppi al corso
course = Course(name="Python")
course.add_group(fullstack)
course.add_group(cloud)
course.add_group(cyber)

# Registrazione degli studenti al corso
course.register(Student(cf="1234", name="Flavio", surname="Maggi", age=29))
course.register(Student(cf="5678", name="Toni", surname="Mancini", age=46))
course.register(Student(cf="9101", name="Luca", surname="Bianchi", age=25))
course.register(Student(cf="2345", name="Marco", surname="Rossi", age=32))
course.register(Student(cf="6789", name="Paolo", surname="Verdi", age=38))
course.register(Student(cf="1011", name="Giulia", surname="Neri", age=21))
course.register(Student(cf="3456", name="Anna", surname="Gialli", age=27))
course.register(Student(cf="7890", name="Maria", surname="Blu", age=35))
course.register(Student(cf="1112", name="Sara", surname="Viola", age=23))
course.register(Student(cf="4567", name="Giovanni", surname="Arancione", age=31))
course.register(Student(cf="8901", name="Andrea", surname="Rosa", age=24))
course.register(Student(cf="1123", name="Matteo", surname="Marrone", age=30))
course.register(Student(cf="5678", name="Toni", surname="Mancini", age=46))

print("### COURSE DETAILS ###")
print(f"Studenti nel gruppo Fullstack: {[student.cf for student in fullstack.get_students()]}")
print(f"Studenti nel gruppo Cloud: {[student.cf for student in cloud.get_students()]}")
print(f"Studenti nel gruppo Cyber: {[student.cf for student in cyber.get_students()]}")