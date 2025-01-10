print([i*i for i in range(10)])
print(sum(i*i for i in range(10)))      # sum of squares

xvec = [10, 20, 30]
yvec = [7, 5, 3]
print([x*y for x,y in zip(xvec, yvec)])
print(x*y for x,y in zip(xvec, yvec))   # dot product

# unique_words = set(word for line in page  for word in line.split())