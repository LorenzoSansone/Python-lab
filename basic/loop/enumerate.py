
#BASE VERSION: with len
"""
students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1,students[i])
"""

#SECOND VERSION: with enumeration
students = ["Hermione", "Harry", "Ron"]

for i, student in enumerate(students):
    print(i + 1, student)