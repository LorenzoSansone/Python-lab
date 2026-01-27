# -*- coding: utf-8 -*-
"""
Multi line comment
"""

#Single line comment


#FIRST VERSION
#print("What's your name?")
#input()

#SECOND VERSION
name = input("What's your name? ")
print("Hi " + name + "!")

#print("Hi", name, "!") #Each insert has a space at the end
#print("Hi", name, "!", int(3), float(4.5)) #Insert what you want
print("Hi!", name + "!", "Ciao") # Second argoment has the + inside
#print(f"Hi! {name}") #Other way to pass the var to print

print("Welcome back!", end = " ") #Override the defualt value. Redefine the end character
print("Let's","get back to work",sep = "!!!") #Override sep

print("Good job \"friend\"")


