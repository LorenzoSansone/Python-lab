#MAP: map() function in Python applies a given function to each element of an iterable (list, tuple, set, etc.) 
# and returns a map object (iterator). 
def main():
    yell("This","is","CS50")

#BASE VERSION: without map
"""
def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    
    print(*uppercased) #unpack the list
"""

#SECOND VERSION: with map
def yell(*words):
    uppercased = map(str.upper, words)
    
    print(*uppercased) #unpack the list


if __name__ == "__main__":
    main()