import random
#DEFINITION: The classmethod() is an inbuilt function in Python, which returns a class method for a given function. This means that classmethod() is a built-in Python function that transforms a regular method into a class method. 
#When a method is defined using the @classmethod decorator (which internally calls classmethod()), the method is bound to the class and not to an instance of the class.
#As a result, the method receives the class (cls) as its first argument, rather than an instance (self).
#Something we want functions associated with the class itself

#The most common USE CASES for the @classmethod include
#1) Creating multiple constructors for flexibility in instantiation.
#2) Implementing factory methods to encapsulate complex object creation logic.
#3) Modifying class-level attributes that apply to all instances. Class methods can be used to modify class state. This is particularly useful when you have shared data across instances.

#KEYWORD: @classmethod

#CLASS VARIABLES are all instances of the class share the same copy of this variable.

class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"] #CLASS VARIABLES are shared among the objects

    #We can call this method without instatiate the Hat object first
    @classmethod
    def sort(cls, name): #cls: reference to the class itself
        print(name, "is in", random.choice(cls.houses)) #access to the class variable

#Access to the class method
Hat.sort("Harry")


