class VariableNumberOfArguments:
    def my_function(self, *args):
        for arg in args:
            print(arg, end=" ")
        print()


va = VariableNumberOfArguments()

va.my_function(1, 2, 3)  # Output: 1 2 3
va.my_function('a', 'b', 'c', 'd')  # Output: a b c d

# $ python VariableNumberOfArguments.py 
# 1 2 3 
# a b c d 