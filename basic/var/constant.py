#In Python, constants are variables whose values are intended to remain unchanged throughout a program. 
#They are typically defined using uppercase letters to signify their fixed nature, often with words separated by underscores (e.g., MAX_LIMIT).

#BASE VERSION: constant simple example
"""
MEOWS = 3 #constant

for _ in range(MEOWS):
    print("meow")
"""
        
#SECOND VERSION: constant in the class
class Cat:
    MEOWS = 5

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")

cat = Cat()
cat.meow()
