# This can be useful to close objects and clean up resources:

# Example
# Try to open and write to a file that is not writable:

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

# The program can continue, without leaving the file object open.

# $ python3 file-example.py 
# Something went wrong when writing to the file