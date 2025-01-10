for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
obj = {'one':1, 'two':2}
for key in obj:
    print(key, obj[key])
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')