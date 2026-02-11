#An iterator in Python is an object used to traverse through all the elements of a collection (like lists, tuples or dictionaries)
# one element at a time. It follows the iterator protocol, which involves two key methods:
# __iter__(): Returns the iterator object itself.
# __next__(): Returns the next value from the sequence. Raises StopIteration when the sequence ends.

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
