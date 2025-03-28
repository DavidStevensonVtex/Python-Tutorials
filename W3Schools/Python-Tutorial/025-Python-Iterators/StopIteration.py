# StopIteration

# The example above would continue forever if you had enough next() statements, or if 
# it was used in a for loop.

# To prevent the iteration from going on forever, we can use the StopIteration statement.

# In the __next__() method, we can add a terminating condition to raise an error if the 
# iteration is done a specified number of times:

# Example
# Stop after 20 iterations:

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

# $ python3 StopIteration.py 
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20