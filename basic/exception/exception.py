#SyntaxError -> e.g.: print("hello, world)

#First version
"""
#Put on try the lines that can actually fail 
#so in this case can fail just x = int(input("What's x? "))
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")

print(f"x is {x}") 
#It works just if int(input("What's x? ")) doesn't fail
#if it fail, the input's value is not copied on the variable x because the right part failed (error raised and catched)
#if it fail, the whole process is interrupted by error so the assignment doesn't occur.
#if the value error happens before the assignment, the assignment doesn't occur
"""

#Second version
"""
try:
    x = int(input("What's x? "))
except ValueError: #if something goes wrong this part is executed to handle the error
    print("x is not an integer")
else: #if the code succeed this part exectued
    print(f"x is {x}")
"""

#Third version
"""
while True: #until the input is correct (break on else branch)
    try:
        x = int(input("What's x? "))
    except ValueError: #if something goes wrong this part is executed to handle the error
        print("x is not an integer")
    else: #if the code succeed this part exectued
        break
print(f"x is {x}")
"""


