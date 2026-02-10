#GETTER and SETTER in Pythonic way
#PRIVATE variable

class Student():
    def __init__(self, name, age):
        self.name = name #setter called
        self.age = age   #setter called
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
    
    #getter for name
    @property
    def name(self):
        print("Getter called for name")
        return self.__name
    
    #setter for name
    @name.setter
    def name(self, name):
        print("Setter called for name")
        self.__name = name
    
    #getter for age
    @property
    def age(self):
        print("Getter called for age")
        return self.__age
    
    #setter for age
    @age.setter
    def age(self, age):
        print("Setter called for age")
        self.__age = age

def main():
    #Init student
    print("Start init student")
    student = Student("Gianni",23) #getter called in init method
    print("End init student", end = "\n\n")

    #Setter called
    print("Student set attributes")
    student.name = "Gianni 2"
    student.age = 24
    print()

    #Getter called
    print("Student get attributes")
    print(student.name)
    print(student.age)
    print()

    #Getter called
    print("Print student")
    print(student)

if __name__ == "__main__":
    main()