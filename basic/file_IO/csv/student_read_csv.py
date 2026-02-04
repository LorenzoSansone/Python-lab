#BASE version to read csv
"""
with open("students.csv","r") as file:
    for line in file:
        name, house = line.rstrip().split(",") #split let to split every row considering the coma
        print(f"{name} is in {house}")
"""

#SECOND version: keep tracking of each data
"""
students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["house"] = house
        students.append(student)

for student in students:
    print(f"{student["name"]} is in {student["house"]}")
"""

#THIRD version: compact and ordered
"""
students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name":name, "house":house}
        students.append(student)

#Get the name (for sorting)
def get_name(student):
    return student["name"]

#Get the house (for sorting)
def get_house(student):
    return student["house"]

#print and sort by key
for student in sorted(students, key=get_name, reverse=True): #key: specify a function to execute to decide the order
    print(f"{student["name"]} is in {student["house"]}")
"""

#FOURTH version: compact and ordered with lambda
students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name":name, "house":house}
        students.append(student)

#print and sort by key
for student in sorted(students, key=lambda student: student["name"]): #key: specify a function to execute to decide the order
    print(f"{student["name"]} is in {student["house"]}")
