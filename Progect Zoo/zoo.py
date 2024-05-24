class Animal:

    """
    This class rappresent an animal with a name(str), species(str), age(int), height(float), width(float), habitat(str)
    """
    
    def __init__(self, name: str, species: str, age: int, height:float, width:float, preferred_habitat:str) -> None:
        
        self.name: str = name
        self.species: str = species
        self.age: int = age
        self.height: float = height
        self.width: float = width
        self.preferred_habitat: str = preferred_habitat
        self.health: float = round(100 * (1 / age), 3)
        self.fence: Fence = None
   
class Fence:

    '''
    This class rappresent a fence with an area(float), temperature(float), habitat(str), list of animals(list)   
    '''

    def __init__(self, area: float, temperature: float, habitat: str, animals: list[Animal] = []) -> None:
        self.area: float = area
        self.temperature: float = temperature
        self.habitat: str = habitat
        self.animals: list[Animal] = []
        self.animals = [animal for animal in animals if self.is_available(animal) and animal.preferred_habitat == habitat]
        for animal in self.animals:
            self.animals.append(animal)
        
    def is_available(self, add_animal: Animal, feed: bool = False) -> bool:
        '''
        This def controll if there is enough space in the fence and return a bool (true if there is spase, false if not space)
        '''
        available = self.area - sum(animal.width*animal.height for animal in self.animals if self.animals)
        if feed:
            return available-(add_animal.width*add_animal.height + (add_animal.width*2/100)*(add_animal.height*2/100)) > 0
        return available-add_animal.width*add_animal.height > 0


class ZooKeeper:
    
    '''
    This class represents a zookeeper with a name, surname and an id
    '''
    
    def __init__(self, name: str, surname: str, id: str) -> None:
        self.name: str = name
        self.surname: str = surname
        self.id: str = id
    
    def add_animal(self, animal: Animal, fence: Fence) -> None:
        
        '''
        This method adds an animal to a specified fence.
        '''
        
        if not animal.fence:
            if fence.habitat == animal.preferred_habitat:
                if fence.is_available(animal):
                    fence.animals.append(animal)
                    animal.fence = fence
                else:
                    print("There is no area in this Fence.")
            else:
                print("This animal doesn't like this Fence. Try another one")
        else:
            print("This animal is alredy in thi Fence.")

    def remove_animal(self, remove_animal: Animal, fence: Fence) -> None:
        
        '''
        This method removes an animal from a specified fence.
        '''
        
        animals: list = fence.animals
        animals_names: list = [animal.name for animal in animals]
        if animals:
            if remove_animal.fence == fence:
                index: int = animals_names.index(remove_animal.name)
                del animals[index]
                remove_animal.fence = None
            else:
                print(f"\nThere is no animal called {remove_animal.name} in this fence.")
        else:
            print("\nThe fence is empty.")
    
    def feed(self, feed_animal: Animal) -> None:
        
        '''
        This method feeds an animal.
        '''
        
        if feed_animal.fence:
            if feed_animal.fence.is_available(feed_animal, feed=True):
                feed_animal.width += feed_animal.width/50
                feed_animal.height += feed_animal.height/50
                feed_animal.health += feed_animal.health/100
            else:
                print(f"\nThe animal can't be fed.")
        else:
            print("\n No animal found")
    
    def clean(self, fence: Fence) -> float:
        
        '''
        Returns the time that the zookeper needs to clean the Fence
        '''
        
        animals: list = fence.animals
        occupied: float = sum(animal.width*animal.height for animal in animals)
        available: float = fence.area - occupied
        time: float = occupied if available == 0 else available/occupied
        return time

class Zoo:
    
    '''
    This class represents a zoo with a list of Fence and a list of ZooKeeper
    '''

    def __init__(self, fences: list[Fence], zoo_keepers: list[ZooKeeper]) -> None:
        self.fences: list[Fence] = fences
        self.zoo_keepers: list[ZooKeeper] = zoo_keepers

    def describe_zoo(self) -> None:
        
        '''
        This method shows every information about the zookeepers, the fences and the animals
        '''
        
        print("\n\nGuardians:")
        for keeper in self.zoo_keepers:
            print(f"\nZooKeeper(name={keeper.name}, surname={keeper.surname}, id={keeper.id})")
        print("\nFences:")
        for fence in self.fences:
            print(f"\nFence(area={fence.area}, temperature={fence.temperature}, habitat={fence.habitat})", end="\n\n")
            if fence.animals:
                print("with animals:\n")
                for animal in fence.animals:
                    print(f"Animal(name={animal.name}, species={animal.species}, age={animal.age})",end="\n\n")
            print("#"*30)
        print(end="\n\n")

