#LIST COMPREHENSIONS: List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
#newlist = [expression for item in iterable if condition == True]

#FIRST VERSION
"""
def main():
    yell("This","is","CS50")

def yell(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)

if __name__ == "__main__":
    main()
"""

#SECOND VERSION
students = [
    {"name": "Hermione", "house":"Gryffindor"},
    {"name": "Harry", "house":"Gryffindor"},
    {"name": "Ron", "house":"Gryffindor"},
    {"name": "Draco", "house":"Slytherin"},
    {"name": "Padma", "house":"Ravenclaw"}
]

gryffindors = [student["name"] for student in students if student["house"] == "Gryffindor"]
print(gryffindors)