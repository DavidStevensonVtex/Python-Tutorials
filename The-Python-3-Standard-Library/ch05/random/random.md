# [Chapter 5: Mathematics](https://pymotw.com/3/numeric.html)

## [5.3 random — Pseudorandom Number Generators](https://pymotw.com/3/random/index.html)

Purpose:	Implements several types of pseudorandom number generators.

The random module provides a fast pseudorandom number generator based on the Mersenne Twister algorithm. Originally developed to produce inputs for Monte Carlo simulations, Mersenne Twister generates numbers with nearly uniform distribution and a large period, making it suited for a wide range of applications.

### 5.3.1 Generating Random Numbers

The random() function returns the next random floating point value from the generated sequence. All of the return values fall within the range 0 \<= n \< 1.0.

```
# random_random.py
import random

for i in range(5):
    print("%04.3f" % random.random(), end=" ")
print()
```

Running the program repeatedly produces different sequences of numbers.

```
$ python3 random_random.py
0.464 0.607 0.269 0.439 0.639 
```

To generate numbers in a specific numerical range, use uniform() instead.

```
# random_uniform.py
import random

for i in range(5):
    print("{:04.3f}".format(random.uniform(1, 100)), end=" ")
print()
```

Pass minimum and maximum values, and uniform() adjusts the return values from random() using the formula min + (max - min) * random().

```
$ python3 random_uniform.py
91.744 41.299 5.352 26.174 47.688
```

### 5.3.2 Seeding

random() produces different values each time it is called and has a very large period before it repeats any numbers. This is useful for producing unique values or variations, but there are times when having the same data set available to be processed in different ways is useful. One technique is to use a program to generate random values and save them to be processed by a separate step. That may not be practical for large amounts of data, though, so random includes the seed() function for initializing the pseudorandom generator so that it produces an expected set of values.

```
# random_seed.py
import random

random.seed(1)

for i in range(5):
    print("{:04.3f}".format(random.random()), end=" ")
print()
```

The seed value controls the first value produced by the formula used to produce pseudorandom numbers, and since the formula is deterministic it also sets the full sequence produced after the seed is changed. The argument to seed() can be any hashable object. The default is to use a platform-specific source of randomness, if one is available. Otherwise, the current time is used.

```
$ python3 random_seed.py
0.134 0.847 0.764 0.255 0.495 
$ python3 random_seed.py
0.134 0.847 0.764 0.255 0.495
```