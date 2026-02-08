
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

if __name__ == "__main__":
    main()
