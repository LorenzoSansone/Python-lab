import argparse

#Argparse: The argparse module makes it easy to build user-friendly command-line interfaces.
#EXAMPLE: python argparse.py -n 3

#Parse the arguments.
#-n, -d, -s, etc can be in any order
parser = argparse.ArgumentParser()

#"help": used in order to see the comment in doc python argparse.py -h
#"default": default value of -n when we launch the program. The default value is used when the option string was not present at the command line:
#"type": The type keyword for add_argument() allows any necessary type-checking and type conversions to be performed
parser.add_argument("-n", default=1, help = "number of times to meow", type=int) 
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")

