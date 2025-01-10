def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print(char, end=" ")
print()

# $ python generators.py
# f l o g 