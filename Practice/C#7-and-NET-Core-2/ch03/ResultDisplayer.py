from multipledispatch import dispatch


class ResultDisplayer:
    @dispatch(str)
    def DisplayResult(result):
        print(f"string: {result}")
    
    @dispatch(int)
    def DisplayResult(result):
        print(f"integer: {result}")

rd = ResultDisplayer()
rd.DisplayResult("The rain in Spain")

rd.DisplayResult(1234)

# $ python ResultDisplayer.py 
# string: The rain in Spain
# integer: 1234