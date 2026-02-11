#Dictionary comprehension is used to create a dictionary in a short and clear way. 

#BASE VERSION: without comprehesion
"""
students = ["Hermione", "Harry", "Ron"]
gryffindors = []

for student in students:
    gryffindors.append({"name":student, "house":"Gryffindor"})

print(gryffindors)
"""

#SECOND VERSION: list comprehension
"""
students = ["Hermione", "Harry", "Ron"]
gryffindors = [{"name":student, "house":"Gryffindor"} for student in students]

print(gryffindors)
"""

#THIRD VERSION: dict comprehension
students = ["Hermione", "Harry", "Ron"]
gryffindors = {student: "Gryffindor" for student in students}

print(gryffindors)