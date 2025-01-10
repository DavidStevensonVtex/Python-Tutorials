s = 'abc'
it = iter(s)
print("it", it)
print("next(it)", next(it))
print("next(it)", next(it))
print("next(it)", next(it))
print("next(it)", next(it))

# $ python iter-next-StopIteration.py 
# it <str_ascii_iterator object at 0x000002790A65A110>
# next(it) a
# next(it) b
# next(it) c
# Traceback (most recent call last):
#   File "D:\drs\Python\GitHub\Python-Tutorials\Python-Tutorial\009-Classes\iter-next-StopIteration.py", line 7, in <module>
#     print("next(it)", next(it))
#                       ^^^^^^^^
# StopIteration