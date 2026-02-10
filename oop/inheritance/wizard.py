#inheritance: define multiple classes that are related one another

#Wizard has the common attribute between Student and Professor
class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name
    
    ...

#Student inherits from Wizard
#Student is a subclass of Wizard
#Wizard is the superclass of Student

class Student(Wizard): 
    def __init__(self, name, house):
        super().__init__(name) #reference to the superclass (Wizard). The super() function is used to give access to methods and properties of a parent or sibling class.
        self.house = house

    ...

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    
    ...

wizard = Wizard("Albus")

student = Student("Harry", "Gryffondor")
professor = Professor("Severus","Defence Against the Dark Arts")
