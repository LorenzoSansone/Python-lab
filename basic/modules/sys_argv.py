import sys
#sys.argv[0] -> name of the program
#sys.argv[1] -> first argument

#BASE version
"""
print("Hello, my name is", sys.argv[1]) #call python sys_argv Matteo
"""

#SAFE version
"""
try:
    print("Hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")
"""

#Input note: python sys_argv.py "Rossi Giacomo" is considered as a single arguments

#DEFENSIVE version -> I want exactly 2 arguments
"""
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("Hello, my name is", sys.argv[1]) 
"""

#MODULAR version using sys.exit: allowing the user to gracefully terminate the execution
"""
#MODULE 1: Check for errors
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

#MODULE 2: Print name tag
print("Hello, my name is", sys.argv[1]) 
"""

#ITERATE version
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for i, arg in enumerate(sys.argv[1:]): #sys.argv[1:] -> we don't want the first element of the list
    print(i, ") ",arg, sep = "")


