
#BASE VERSION
#we use TUPLE: A tuple is a collection which is ordered and UNCHANGEABLE. tuples are used to store multiple items in a single variable. 
"""
def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    name  = input("Name: ")
    house = input("House: ")
    return name, house #return a TUPLE (it's a single value) -> we could use (name, house) -> more explicit
    #return [name, house] #ALTERNATIVE: return a LIST
    #ALTERNATIVE: we could use a DICTIONARY because with list and tuple we don't have to remember the position of name and house on the structure
"""

#SECOND VERSION: use classes
#We need class to create our own object
"""
class Student: #use Capital letter for classes
    ... #It indicates that a function, class or method is defined but not yet implemented

def main():
    student  = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    student = Student() #create a new object from classes (classes is a blueprint)
    student.name = input("Name: ")
    student.house = input("House: ")
    return student
"""

#THIRD VERSION: use classes with METHODS -> determine behaviour
#the keyworld "self" gives acces to the current object that is just created
"""
class Student: #Every student will be STRUCTURED the same. We can customize the CONTENT
    def __init__(self, name, house): #instance method -> let initializa the conent of the classes
        self.name = name
        self.house = house

def main():
    student  = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House:")
    student = Student(name, house) #passes name and house as argument
    return student
"""
    

#FOURTH VERSION -> the classes CHECK the input and personalize print
"""
class Student: 
    def __init__(self, name, house=None): #we can make optional some input argument
        if not name: #name is blank?
            raise ValueError("Missing name") #we have to catch with try expect
        if house not in ["Gryffondor", "Hufflepuff", "Ravenclaw", "Slythering"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
    
    #Perzonalize the method for printing
    def __str__(self):
        return f"{self.name} from {self.house}"

def main():
    student  = get_student()
    print(student) #we can print directly the student using "__str__" method

def get_student():
    name = input("Name: ")
    house = input("House:")
    return Student(name, house) #passes name and house as argument
"""

#FIFTH version: add methods (CUSTOM function)
"""
class Student: 
    def __init__(self, name, house, patronus): #we can make optional some input argument
        if not name: #name is blank?
            raise ValueError("Missing name") #we have to catch with try expect
        if house not in ["Gryffondor", "Hufflepuff", "Ravenclaw", "Slythering"]:
            raise ValueError("Invalid house")
    
        self.name = name
        self.house = house
        self.patronus = patronus
    
    #Perzonalize the method for printing
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    def charm(self): #Custom function
        match self.patronus:
            case "Stag":
                return "0"
            case "Otter":
                return "1"
            case "Jake Russel terrier":
                return "2"
            case _: #execute when there are not other matches:
                return "/"

def main():
    student  = get_student()
    print("Expecto Patronum!")
    print(student.charm())

def get_student():
    name = input("Name: ")
    house = input("House:")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)
"""

#SIXTH VERSION: properties
#GETTER and SETTER are methods used to access and update the attributes of a class.
#these methods provide a way to define controlled access to the attributes of an object, thereby ensuring the integrity of the data. 
#By default, attributes in Python can be accessed directly. However, this can pose problems when attributes need validation or transformation before being assigned or retrieved.

#Three main ways:
# 1) use getter and setter without any protection and using public/non-public variables
# 2) use the python function called "property()"
# 3) use the Pythonic way: @property decorators:
#  a) @property for getter
#  b) @<property_name>.setter for setter

#Three main ways to define a variables:
# 1)Public Variables: Accessible from anywhere; no underscores.
# 2)Protected Variables: Accessible within the class and its subclasses; prefixed with a single underscore (_).
# 3) Private Variables: Accessible only within the class; prefixed with a double underscore (__).


#If we have instance variable called "name" or "house", we can't have functions with the same name (so in this example we change the name of the instance variable)

class Student: 
    def __init__(self, name, house): #we can make optional some input argument    
        self.name = name
        self.house = house #in this line the setter for house will be called and the input checked
        #In this line we don't use _house otherwise the setter isn't called
    
    #Perzonalize the method for printing
    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name: #if name is blank
            raise ValueError("Missing name")
        self._name = name

    #getter
    @property
    def house(self):
        return self._house
    
    #Setter: in this way when we call 'student.house = "Number Four" ', this function is called
    #WHEN called: everytime is called student.house 
    @house.setter
    def house(self, house):
        if house not in ["Gryffondor", "Hufflepuff", "Ravenclaw", "Slythering"]:
           raise ValueError("Invalid house")
        self._house = house

def main():
    student  = get_student()
    #student.house = "Number Four" #try to change the variable but it will fail due to the check in the setter
    print(student)

    #the underline attributes implemented in the instance variable is called "_house" and we can call it
    #student._house = "Number Four" #it works and the getter isn't called

def get_student():
    name = input("Name: ")
    house = input("House:")
    return Student(name, house) 

if __name__ == "__main__":
    main()
