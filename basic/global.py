#GLOBAL VARIABLE

#Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.
#Global variables can be used by everyone, both inside of functions and outside.

# 1)use the "global" keyword if you want to change a global variable inside a function.
# 2)To create a global variable inside a function, you can use the "global" keyword.
# 3) If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. 
# The global variable with the same name will remain as it was, global and with the original value.

balance = 0

def main():
    print("Balance:", balance) #we can read the global variable without "global" keyword
    deposit(100)
    withdraw(50)
    print("Balance:", balance)

def deposit(n):
    global balance
    balance += n

def withdraw(n):
    global balance
    balance -= n

if __name__ == "__main__":
    main()