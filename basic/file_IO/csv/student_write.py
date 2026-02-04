import csv

#BASE VERSION
"""
name = input("What's your name? ")
home = input("What's your home? ")

with open("students_write.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])
"""

#SECOND VERSION    
name = input("What's your name? ")
home = input("What's your home? ")

with open("students_write.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name","home"])
    writer.writerow({"name":name, "home":home})
    #writer.writerow({"home":home, "name":name}) #EQUIVALENT: the order doesn't matter