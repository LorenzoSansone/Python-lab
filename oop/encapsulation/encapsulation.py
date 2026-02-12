#Encapsulation is about protecting data inside a class. Encapsulation means hiding internal details of a class and only exposing what's necessary
#It means keeping data (properties) and methods together in a class, while controlling how the data can be accessed from outside the class.
#This prevents accidental changes to your data and hides the internal details of how your class works.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age # Private property

p1 = Person("Emil", 25)
print(p1.name)
print(p1.__age) # This will cause an error