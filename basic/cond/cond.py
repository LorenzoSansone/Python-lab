# -*- coding: utf-8 -*-

#IF - ELIF - ELSE
"""
x = int(input("What's x?"))
y = int(input("What's y?"))

#elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else: #we could obmit it because it logically irrelevant. At this point is forced to be x == y
    print("x is equal to y")
"""

#OR
"""
x = int(input("What's x?"))
y = int(input("What's y?"))

if x < y or x >y:
    print("x is not equal to y")
else:
    print("x is equal to y")
"""

#!=
"""
x = int(input("What's x?"))
y = int(input("What's y?"))

if x!=y:
    print("x is not equal to y")
else:
    print("x is equal to y")
"""

#AND
"""
score = int(input("Score: "))
if score >= 90 and score <= 100:
    print("Grade A")
elif score >= 80 and score < 90:
    print("Grade B")
elif score >= 70 and score < 80:
    print("Grade C")
elif score >= 60 and score < 70:
    print("Grade D")
elif score < 60:
    print("Grade F")
"""

#AND - other solution
score = int(input("Score: "))
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("Grade F")

