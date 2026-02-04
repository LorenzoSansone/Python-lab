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
email = input("What's your email? ").strip()

if re.search("@",email):
    print("Valid")
else:
    print("Invalid")
