def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")


#var __name__:
#If the source file is executed as the main program,
#the interpreter sets the __name__ variable to have a value "__main__". 
#If this file is being imported from another module, __name__ will be set to the module's name.
if __name__ == "__main__":
    main()
