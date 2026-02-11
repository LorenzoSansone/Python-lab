#Type hints are a feature in Python that allow developers to annotate their code with expected types for variables and function arguments. 
#This helps to improve code readability and provides an opportunity to catch errors before runtime using type checkers like mypy.

#mypy type_hints_mypy.py (file name) -> should catch error before runtime (if type hints are used)

#BASE VERSION: this script has an error. The goal is to discover this error using the type hints and mypy before running the code.
"""
def meow(n: int): #n should be an int (but this constraint is not enforced by the language)
    for _ in range(n):
        print("meow")

number: int = input("Number: ") #annotated also this variable (number)
meow(number)
"""

#SECOND VERSION
"""
def meow(n: int) -> None: #mypy will detect that this function doesn't return values. mypy wil show "meow" does not return a value (it only ever returns None) 
    for _ in range(n):
        print("meow")

number: int = int(input("Number: ")) 
meows: str = meow(number)
print(meows)
"""

#THIRD VERSION
def meow(n: int) -> str: 
    return "meow\n" * n

number: int = int(input("Number: ")) 
meows: str = meow(number)
print(meows, end = "")

#THIRD VERSION
#The add_numbers function expects two integers (x: int, y: int) and returns an integer (-> int).
"""
def add_numbers(x: int, y: int) -> int:
    return x + y
"""