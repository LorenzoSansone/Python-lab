#The filter() function returns an iterator where the items are filtered through a function to test if the item is accepted or not.
#filter() function is used to extract elements from an iterable (like a list, tuple or set) that satisfy a given condition. 
#It works by applying a function to each element and keeping only those for which function returns True.
students = [
    {"name": "Hermione", "house":"Gryffindor"},
    {"name": "Harry", "house":"Gryffindor"},
    {"name": "Ron", "house":"Gryffindor"},
    {"name": "Draco", "house":"Slytherin"},
    {"name": "Padma", "house":"Ravenclaw"}
]

def is_gryffindor(s):
    if s["house"] == "Gryffindor":
        return True
    else:
        return False
    
    #return s["house"] == "Gryffindor" #SHORTER ALTERNATIVE 
    
gryffindors = filter(is_gryffindor, students)
#gryffindors = filter(lambda s: s["house"] == "Gryffindor", students) #ALTERNATIVE without the explict function is_gryffindor

for gryffindor in gryffindors:
    print(gryffindor["name"])

