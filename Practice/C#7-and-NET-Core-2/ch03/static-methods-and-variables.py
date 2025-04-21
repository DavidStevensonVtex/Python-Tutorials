class MyClass:
    b = "Woof! Meow!"   # static initialization
    @staticmethod
    def myFunction(a):
        print(f"myFunction: a: {a} b: {MyClass.b}");

MyClass.myFunction("cats and dogs")

# $ python static-methods-and-variables.py 
# myFunction: a: cats and dogs b: Woof! Meow!