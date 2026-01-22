# -*- coding: utf-8 -*-


name = input("What's your name?").strip().title()

#Split user's name into name and last name
first, last = name.split(" ")

print(f"Hello, {first}")
