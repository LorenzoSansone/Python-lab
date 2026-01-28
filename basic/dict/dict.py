students_list = ["Hermione", "Harry", "Ron", "Draco"]
houses_list = ["Gryffindor","Gryffindor","Gryffindor", "Slytherin"]

#Compress way to init a dict
#students = dict(zip(students_list, houses_list))

"""
students = {"Hermione": "Gryffindor",
            "Harry":"Gryffindor",
            "Ron": "Gryffindor",
            "Draco": "Slytherin"}
"""
            
#Print one element
# print(students["Ron"])

#PRINT all 1# way
"""
for student in students.keys():
    print(student)
"""

#PRINT all 2# way
"""
for student in students:
    print(student)
"""

#PRINT all the dict
for student in students:
    print(student, students[student], sep = ", ")

