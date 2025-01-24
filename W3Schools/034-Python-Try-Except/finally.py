# Finally

# The finally block, if specified, will be executed regardless if the try block raises an error or not.

# Example
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

# $ python3 finally.py 
# Something went wrong
# The 'try except' is finished