import csv #use csv library

#BASE version
students = []
with open("students_home.csv") as file:
    reader = csv.reader(file) #read the csv file
    for name, home in reader:
        students.append({"name":name, "home":home})

#print and sort by key
for student in sorted(students, key=lambda student: student["name"]): #key: specify a function to execute to decide the order
    print(f"{student["name"]} is from {student["home"]}")


