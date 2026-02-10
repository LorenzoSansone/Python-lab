#Operator overloading in Python allows same operator to work in different ways depending on data type.

#GOAL: we would like to ADD two Vault together
#This class represents a Bank Vault
class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
    
    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    #add the content of two vaults
    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)


potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

#BASE VERSION: without overloading operator
"""
galleons = potter.galleons + weasley.galleons
sickles = potter.sickles + weasley.sickles
knuts = potter.knuts + weasley.knuts
total = Vault(galleons, sickles, knuts)
"""

#SECOND VERSION: with overloading operator
total = potter + weasley

print(total)
