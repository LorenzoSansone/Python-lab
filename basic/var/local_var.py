#Example with local and global variable

A=10

def foo(x):
    return A+x

def fie(y):
    A=100
    return A+y

print(foo(10)) # prints 20
print(fie(10)) # prints 210
print(A) # prints 10