# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 18:53:33 2026

@author: 32057
"""

#Original
"""
name = input("What's your name? ")

if name == "Harry":
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")
"""

#First version
"""
name = input("What's your name? ")

if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")
"""

#MATCH 
"""
name = input("What's your name? ")

match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _: #In case the previous cases fail
        print("Who?")

"""
#MATCH more efficient
name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron": #more short method
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _: #In case the previous cases fail
        print("Who?")

