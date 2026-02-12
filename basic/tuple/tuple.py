#Example of tuple definition
"""
(10.3, 100, 'simone')
(3,)
()
(1, 2, (100,200), 3)
(10, 20,)
10,20
"""

#Any operation creates a new object!
T = (1,2,3)
print(id(T))

T = T + (4,5)
print(id(T))
