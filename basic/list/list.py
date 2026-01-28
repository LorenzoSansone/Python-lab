students = ["Hermione", "Harry", "Ron"]

#PRINT an element of list
print(students[0])

#PRINT all the element
for student in students:
    print(student)

#PRINT another way
for i in range(len(students)):
    #print(students[i])
    print(i + 1, ") ",students[i], sep = "")


