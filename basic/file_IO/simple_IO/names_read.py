
#BASE VERSION
"""
with open("names.txt","r") as file: #r: read (defaul value)
    lines = file.readlines() #read all the lines of the file and store into a list

for line in lines:
    #print(f"hello, {line}", end = "")
    print(f"hello", line.rstrip()) #other possibility to the previous print
"""

#SECOND VERSION: compact version
"""
with open("names.txt", "r") as file:
    for line in file:
        print("hello,",line.rstrip())
"""

#THIRD VERSION: read and sort
"""
names = []

with open("names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")
"""

#FOURTH VERSION: read and sort more compact
"""
with open("names.txt", "r") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())
"""


