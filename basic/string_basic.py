# -*- coding: utf-8 -*-

name = input("What's your name? ")

#Remove whitespace from str (left and right - not in between)
#name = name.strip()

#Capitalize the first character of the string
#name = name.capitalize()

#Capitalize the first string of EACH world of the string (separate by space)
#name = name.title()

#Do in one line
name = name.strip().title()

#Do the task in one line
#name = input("What's your name?").strip().title()

print(f"hello, {name}", end = "")


