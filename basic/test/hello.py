def main():
    name = input("What's your name? ")
    print(hello(name))

#LESS TESTABLE VERSION: in this case there isn't any return keyworld
#we should test the side effect of the print (side effect: it prints on the screen)
"""
def hello(to="world"):
    print(f"hello, {to}")
"""

#MORE TESTABLE VERSION: it's better testable returning the string that should be printed
def hello(to="world"):
    return f"hello, {to}"


if __name__ == "__main__":
    main()