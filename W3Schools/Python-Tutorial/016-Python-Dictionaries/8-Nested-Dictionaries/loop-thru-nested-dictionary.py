# Loop Through Nested Dictionaries
# You can loop through a dictionary by using the items() method like this:

# Example
# Loop through the keys and values of all nested dictionaries:

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])

# $ python3 loop-thru-nested-dictionary.py 
# child1
# name: Emil
# year: 2004
# child2
# name: Tobias
# year: 2007
# child3
# name: Linus
# year: 2011