# -*- coding: utf-8 -*-

#SUM + ROUND
"""
x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y) #round to the nearest integer
z_round = round(x + y,1) #round to nearest number of digit

print(f"sum rounded {z} ({z_round})")
"""

#DIVISION + ROUND
x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x / y, 2) #round to nearest number of digit

print(z)
#print(f"{z:.2f}") #like round
