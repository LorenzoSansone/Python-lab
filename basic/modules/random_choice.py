import random #import everything from the module random
from random import choice #keyword "from" import function from a module (more ligther)
#but now we have to pay attention when we have another function with the same name


#BASE
coin = random.choice(["heads","tails"])

#USING THE KEYWORD from random import choice (it works as before)
coin_1 = choice(["heads","tails"])

print(coin_1)