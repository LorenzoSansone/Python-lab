import re # library that has the capabilities to define, check or replace pattern

#BASE version: without regex
#problems: the input could just be "@" but the e-mail is invalid
"""
email = input("What's your email? ").strip()

if "@" in email: #check if @ is in the email string
    print("Valid")
else:
    print("Invalid")
"""

#SECOND version: better but we have to improve the solution
"""
email = input("What's your email? ").strip()

username, domain = email.split("@")

if (username) and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")
"""

#THIRD version: with regex
'''
email = input("What's your email? ").strip()

#Pattern ^.+@.+\.edu$ means:
#0) ^ -> start of the string
#1) . -> Any character except a newline
#2) + -> one or more times
#3) @ -> single character @
#4) . -> Any character except a newline
#5) + -> one or more times
#6) \. -> match exactly a dot (the slash is an escape character)  
#7) edu -> match the string 'edu' "
#8) $ -> end of the string

#Equivalent pattern is ^..*@..*\.edu$

if re.search(r"^.+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
'''

#FOURTH version: regex
"""
email = input("What's your email? ").strip()

#Pattern ^[^@]+@[^@]+\.edu$ means:
#0) ^ -> start of the string
#1) [^@] -> Any character except a @
#2) + -> one or more times
#3) @ -> single character @
#4) [^@] -> Any character except a @
#5) + -> one or more times
#6) \. -> match exactly a dot (the slash is an escape character)  
#7) edu -> match the string 'edu' "
#8) $ -> end of the string

if re.search(r"^[^@]+@[^@]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
"""


#FIFTH version: regex
"""
email = input("What's your email? ").strip()

#Pattern ^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$ means:
#0) ^ -> start of the string
#1) [a-zA-Z0-9_] -> set of character allowed: range between (a and z), (A and Z), (0 and 9) and support underscore
#2) + -> one or more times
#3) @ -> single character @
#4) [a-zA-Z0-9_] -> same as before
#5) + -> one or more times
#6) \. -> match exactly a dot (the slash is an escape character)  
#7) edu -> match the string 'edu' "
#8) $ -> end of the string

#\w: word charcater (alphanumeri symbol - included the underscore) 
#OTHER EQUIVALENT SOLUTION: ^\w+@\w.edu$ 
#OTHER SOLUTION: ^\w+@\w.(com|edu|org|it)$ -> more flexible for the final part of the email

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
"""

#SIXTH version: regex
email = input("What's your email? ").strip()

#Pattern ^\w+@(\w+\.)?\w+\.edu$ means:
#0) ^ -> start of the string
#1) \w -> \w: word charcater (alphanumeri symbol - included the underscore)
#2) + -> one or more times
#3) @ -> single character @
#4) (\w+\.)-> one or more alphanumeric character and dot as a whole -> e.g: abc. or benigni. or ecc
#5) ? -> zero or one time of (\w+\.) (so the subdomain is optional)
#6) \w+ -> one or more alphanumeric characters
#7) \. -> match exactly a dot (the slash is an escape character)  
#8) edu -> match the string 'edu' "
#9) $ -> end of the string

#Example input: user@domain1.domain2.edu 
#(if you want more domains)

#re.IGNORECASE: ignore the case of the input
if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, flags = re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")



