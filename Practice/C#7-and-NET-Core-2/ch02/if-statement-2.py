input = input("Type in a string: ")
if input == "":
    print("You typed in an empty string")
elif len(input) < 5:
    print("The string had less than 5 characters")
elif len(input) < 10:
    print("The string had at least 5 but less than 10 characters")
print("The string input was ", input)

# $ python if-statement-2.py 
# Type in a string: abc
# The string had less than 5 characters
# The string input was  abc
# $ python if-statement-2.py 
# Type in a string: 
# You typed in an empty string
# The string input was  
# $ python if-statement-2.py 
# Type in a string: abcdef
# The string had at least 5 but less than 10 characters
# The string input was  abcdef
# $ python if-statement-2.py 
# Type in a string: abcdefghijklm
# The string input was  abcdefghijklm