def main():
    x = get_int()
    print(f"x is {x}")

#Base version
"""
def get_int():
    while True: #until the input is correct (break on else branch)
        try:
            x = int(input("What's x? "))
        except ValueError: #if something goes wrong this part is executed to handle the error
            print("x is not an integer")
        else: #if the code succeed this part exectued
            return x
"""

#Shorter version     
def get_int():
    while True: #until the input is correct (break on else branch)
        try:
            return int(input("What's x? "))
        except ValueError: #if something goes wrong this part is executed to handle the error
            pass #catch the error but we pass about compute the error

main()