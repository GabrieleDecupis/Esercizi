# Per creare classi astratte:

from abc import ABC, abstractmethod

# Exercise 1: Creating an Abstract Class with Abstract Methods

# Create an abstract class Shape with an abstract method area and another abstract method perimeter. 
# Then, create two subclasses Circle and Rectangle that implement the area and perimeter methods.

class Shape(ABC):  # per creare una classe astratta devo fare così 

    @abstractmethod # per creare un metodo astratto devo fare così
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, raggio: float):
        self.raggio = raggio

    def area(self) -> float:
        area = 3.14 * (raggio ** 2)
        return area
    
    def perimeter(self) -> float:
        perimeter = 3.14 * raggio * 2
        return perimeter

class Rectangle(Shape):


    def area(base: float, altezza: float) -> float:
        area = base * altezza
        return area
    
    def perimeter(base: float, altezza: float) -> float:
        perimeter = (base + altezza) * 2
        return perimeter
    

rett1 = Rectangle()
A = rett1.area(10.0, 2.0)
print(A)
        
