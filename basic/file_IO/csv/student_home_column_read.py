import csv #use csv library

#BASE version
#if the order of the csv file's column changes with DictReader we can be sure that 
#we don't have to change the code because we use the key to retrieve the data

students = []
with open("students_home_column.csv") as file:
    reader = csv.DictReader(file) #maps the information in each row to a dict whose keys are given by the optional fieldnames parameter.
    for row in reader:
        students.append({"name":row["name"], "home":row["home"]})

#print and sort by key
for student in sorted(students, key=lambda student: student["name"]): #key: specify a function to execute to decide the order
    print(f"{student["name"]} is from {student["home"]}")


