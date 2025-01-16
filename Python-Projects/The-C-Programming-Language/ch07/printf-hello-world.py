s = "hello, world"
print(":%10s:" % s)
print(":%.10s:" % s)
print(":%-10s:" % s)
print(":%.15s:" % s)
print(":%-15s:" % s)
print(":%15.10s:" % s)
print(":%-15.10s:" % s)

# $ python3 printf-hello-world.py 
# :hello, world:
# :hello, wor:
# :hello, world:
# :hello, world:
# :hello, world   :
# :     hello, wor:
# :hello, wor     :

