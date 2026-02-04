#BASE version: without regex
#problems: the input could just be "@" but the e-mail is invalid
'''
email = input("What's your email? ").strip()

if "@" in email: #check if @ is in the email string
    print("Valid")
else:
    print("Invalid")
'''
