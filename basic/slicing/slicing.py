s="bologna BO"

print(s[0:4]) #bolo: it prints from 0 to 3 (index)

#s[ : <end>] starts at 0
print(s[:len(s)])

#s[<start> : ] ends at len(S)+1, last element included
print(s[0:])

print("Overflow:", s[6:100]) #it 100 is too much it doens't raise an error. it prints just the last letter of the string

print("Step:", s[1:9:2]) #with step

print("Step decrement:", s[5:2:-1] )