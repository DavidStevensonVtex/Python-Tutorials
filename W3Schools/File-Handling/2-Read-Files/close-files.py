# Close Files
# It is a good practice to always close the file when you are done with it.

# Example
# Close the file when you are finished with it:

f = open("demofile.txt", "r")
print(f.readline())
f.close()

# Note: You should always close your files. In some cases, due to buffering, 
# changes made to a file may not show until you close the file.