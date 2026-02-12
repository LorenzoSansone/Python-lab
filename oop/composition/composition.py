#It is one of the fundamental concepts of Object-Oriented Programming. 
#In this concept, we will describe a class that references to one or more objects of other classes as an Instance variable. 
#Here, by using the class name or by creating the object we can access the members of one class inside another class. 
#It enables creating complex types by combining objects of different classes. 
#It means that a class Composite can contain an object of another class Component. This type of relationship is known as Has-A Relation.

class Component:

   # composite class constructor
    def __init__(self):
        print('Component class object created...')

    # composite class instance method
    def m1(self):
        print('Component class m1() method executed...')


class Composite:

    # composite class constructor
    def __init__(self):

        # creating object of component class
        self.obj1 = Component()
        
        print('Composite class object also created...')

     # composite class instance method
    def m2(self):
      
        print('Composite class m2() method executed...')

        # calling m1() method of component class
        self.obj1.m1()


# creating object of composite class
obj2 = Composite()

# calling m2() method of composite class
obj2.m2()