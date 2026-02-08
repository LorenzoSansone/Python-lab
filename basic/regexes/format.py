import re
#GOAL: re-format user input in the format that we expect

#BASE VERSION: without regex
#PROBLEM: there could be error -> fragile
"""
name = input("What's your name? ").strip()

if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"

print(f"hello, {name}")
"""

#SECOND VERSION
"""
name = input("What's your name? ").strip()

#represent the pattern: SURNAME NAME
#I'm using the parenthesis for capture purposing
#the '()' parenthesis are used to define a specific group
matches = re.search(r"^(.+), *(.+)$", name) #the SPACE between the name and surname is optional
if matches:
    #last = matches.group(1) #ALTERNATIVE
    #first = matches.group(2) #ALTERNATIVE
    last, first = matches.groups() #return all the groups parenthesis that are captured
    name = f"{first} {last}"
print(f"hello, {name}")
"""

#THIRD VERSION: more compact
#Walrus operator ":=" -> allows you to assign a value to a variable as part of an expression. It helps avoid redundant code when a value needs to be both used and tested in the same expression
name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name):  
    name = matches.group(1) + " " + matches.group(1)
print(f"hello, {name}")

