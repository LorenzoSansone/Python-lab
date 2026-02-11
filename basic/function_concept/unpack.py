#GOAL: unpack the values
#Python provides the concept of packing and unpacking arguments, which allows us to handle variable-length arguments efficiently. 
#This feature is useful when we don’t know beforehand how many arguments will be passed to a function.

#We use * to unpack elements from a list/tuple: It usually works for structure where there is enumeration like list, tuple, etc (not for set)
#We use ** to unpack key-value pairs from a dictionary.
#We use *args (Non-keyword arguments): Packs multiple positional arguments into a tuple.
#We use **kwargs (Keyword arguments): Packs multiple keyword arguments into a dictionary.

#BASE VERSION: verbose
"""
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]
print(total(coins[0], coins[1], coins[2]),"Knuts")
"""

#SECOND VERSION: use unpacking with list
"""
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]

print(total(*coins),"Knuts") #unpack the list with *
"""

#THIRD VERSION: use unpacking with dict -> you have to use **
"""
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = {"galleons": 100, "sickles":50, "knuts":25}

print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts")

print(total(**coins), "Knuts")
"""

#The * operator allows us to pass multiple arguments to a function and pack them into a tuple.
#The ** operator is used to collect multiple keyword arguments into a dictionary.
#FOURTH VERSION: *args
"""
def f(*args, **kwargs):
    print("Positional:",args)

f(100,50,20)
f(100,50,20,4)
"""

#FIFTH VERSION: **kwargs
"""
def f(*args, **kwargs):
    print("Named:",kwargs)
    print("Named galleons:", kwargs["galleons"])

f(galleons=100, sickles=50, knuts= 20)
"""

#SIXTH VERSION: *args and **kwargs
def f(*args, **kwargs):
    print("Positional", args)
    print("Named:",kwargs)

f(10,30,50,100, galleons=100, sickles=50, knuts= 20)


