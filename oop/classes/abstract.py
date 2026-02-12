from abc import ABC,abstractmethod
#An Abstract Base Class (ABC) defines methods that must be implemented by its subclasses, ensuring that the subclasses follow a consistent structure. 
#ABCs allow you to define common interfaces that various subclasses can implement while enforcing a level of abstraction.
#Python provides the abc module to define ABCs and enforce the implementation of abstract methods in subclasses.

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass 

class Dog(Animal):
    def sound(self):
        return "Bark"

#animal = Animal() #ERROR: can't instantiate an abstract method
dog = Dog()
print(dog.sound())