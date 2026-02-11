#DOCSTRING
#How to document the function (it's just a convention)

#1) Declared using triple quotes (' ' ' or " " ").
#2) Written just below the definition of a function, class, or module.
#3) Unlike comments (#), docstrings can be accessed at runtime using __doc__ or help().

def meow(n: int) -> str: 
    """
    Meow n times.

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """
    return "meow\n" * n

number: int = int(input("Number: ")) 
meows: str = meow(number)
print(meows, end = "")

#Explore the documentation
print("Using __doc__:")
print(meow.__doc__)

print("Using help():")
help(meow)