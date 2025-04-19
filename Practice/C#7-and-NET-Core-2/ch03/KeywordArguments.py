class Geometry:
    def MoveAndResize(self, x = 0, y = 0, width=50, height=50):
        print(f"x: {x} y: {y} width: {width} height: {height}")

g = Geometry()
g.MoveAndResize(x = 123, y = 456, width = 789, height = 567)
g.MoveAndResize()

# $ python KeywordArguments.py 
# x: 123 y: 456 width: 789 height: 567
# x: 0 y: 0 width: 50 height: 50