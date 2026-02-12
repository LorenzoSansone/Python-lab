
#LEGB: Searching for a name in the internal state works inside-out:
# 1) Local - Inside the current function
# 2) Enclosing - Inside enclosing functions (from inner to outer)
# 3) Global - At the top level of the module
# 4) Built-in - In Python's built-in namespace

x = "global"

def outer():
  x = "enclosing"
  def inner():
    #nonlocal x #try this to get the value of x from outside the function inner()
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)


#a and w are global variable
#s and x are local to f
#u is local to g
#s and x are non local to g (or: in the enclosing scope)
"""
a=10

def f(s):
    x=20

    def g(u):
        return u
    
    return s+g(x)

w=f(a)
print(w)
"""


#NONLOCAL
#The nonlocal keyword is used to work with variables inside nested functions.
#The nonlocal keyword makes the variable belong to the outer function.
"""
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())
"""

#OTHER EXAMPLE of non local scope
"""
def outer_func():
     # The code block of outer_func() defines its local scope
     # It also defines the enclosing scope of inner_func()
     variable = 100  # Local to outer_func() and nonlocal to inner_func()
     def inner_func():
         # The code block of inner_func() defines its local scope
         print(f"Printing variable from inner_func(): {variable}")

     inner_func()
     print(f"Printing variable from outer_func(): {variable}")
"""