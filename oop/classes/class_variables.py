import random
#GOAL: notice how the class variable works. Just one copy (of the class variable) is created for every object

#CLASS VARIABLES are all instances of the class share the same copy of this variable.
# 1) Defined inside the class but outside all methods
# 2) Accessed using the class name or an object
# 3) Memory is allocated only once

#Define a class with a CLASS VARIABLES
"""
class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"] #CLASS VARIABLES are shared among the objects

#Instantiated 2 objects from class Hat
hat = Hat()
hat1 = Hat()

#Print the list "houses"
print(hat.houses)
print(hat1.houses)

#Remove an item
a = hat.houses.pop()

#Print the list "houses" (class variable)
print(hat.houses)
print(hat1.houses)

#Delete hat1
del hat1

#Instantiated a new object
hat2 = Hat()

#Print the class variable
print(hat2.houses)
"""

#OTHER EXPERIMENT with class attribute
class A:
    class_attr = 10
    
    def __init__(self,par):
        self.x = par

    def inc(self):
        self.x += A.class_attr

    def __str__(self):
        return 'A('+str(self.x)+')'

print(A.class_attr)
a=A(10)
a.inc()
print(a.x)
print(a.class_attr)
A.class_attr=30
print(a.class_attr)

