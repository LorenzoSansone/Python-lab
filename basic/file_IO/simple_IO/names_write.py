#BASE VERSION
#open: we can read info from a file or write info to a file
#In this case everytime that we open the file and we write into it
#the file's content will be recreated (overwrite the file each time we run the program)
"""
name = input("What's your name? ")

file = open("names.txt","w")#w: write
file.write(name)
file.close()
"""

#SECOND VERSION
"""
name = input("What's your name? ")

file = open("names.txt","a")#a: append -> add to the bottom of the file
#file.write(name) #the names are written in concatenation (no newline)
file.write(f"{name}\n") #new line for each name
file.close()
"""

#THIRD VERSION
name = input("What's your name? ")

with open("names.txt","a") as file:#open and close automaticcaly a file
    file.write(f"{name}\n")

