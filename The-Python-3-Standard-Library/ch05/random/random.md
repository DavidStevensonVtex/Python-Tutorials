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

### 5.3.3 Saving State

The internal state of the pseudorandom algorithm used by random() can be saved and used to control the numbers produced in subsequent runs. Restoring the previous state before continuing reduces the likelihood of repeating values or sequences of values from the earlier input. The getstate() function returns data that can be used to re-initialize the random number generator later with setstate().

```
# random_state.py
import random
import os
import pickle

if os.path.exists("state.dat"):
    # Restore the previously saved state
    print("Found state.dat, initializing random module")
    with open("state.dat", "rb") as f:
        state = pickle.load(f)
    random.setstate(state)
else:
    # Use a well-known start state
    print("No state.dat, seeding")
    random.seed(1)

# Produce random values
for i in range(3):
    print("{:04.3f}".format(random.random()), end=" ")
print()

# Save state for next time
with open("state.dat", "wb") as f:
    pickle.dump(random.getstate(), f)

# Produce more random values
print("\nAfter saving state:")
for i in range(3):
    print("{:04.3f}".format(random.random()), end=" ")
print()
```

The data returned by getstate() is an implementation detail, so this example saves the data to a file with pickle but otherwise treats it as a black box. If the file exists when the program starts, it loads the old state and continues. Each run produces a few numbers before and after saving the state, to show that restoring the state causes the generator to produce the same values again.

```
$ python3 random_state.py
No state.dat, seeding
0.134 0.847 0.764 

After saving state:
0.255 0.495 0.449 
```

### 5.3.4 Random Integers

random() generates floating point numbers. It is possible to convert the results to integers, but using randint() to generate integers directly is more convenient.

```
# random_randint.py
import random

print("[1, 100]:", end=" ")

for i in range(3):
    print(random.randint(1, 100), end=" ")

print("\n[-5, 5]:", end=" ")
for i in range(3):
    print(random.randint(-5, 5), end=" ")
print()
```

The arguments to randint() are the ends of the inclusive range for the values. The numbers can be positive or negative, but the first value should be less than the second.

```
$ python3 random_randint.py
[1, 100]: 54 81 95 
[-5, 5]: -4 3 -4 
```

randrange() is a more general form of selecting values from a range.

```
# random_randrange.py
import random

for i in range(3):
    print(random.randrange(0, 101, 5), end=" ")
print()
```

randrange() supports a step argument, in addition to start and stop values, so it is fully equivalent to selecting a random value from range(start, stop, step). It is more efficient, because the range is not actually constructed.

```
$ python3 random_randrange.py
100 60 60 
```

### 5.3.5 Picking Random Items

One common use for random number generators is to select a random item from a sequence of enumerated values, even if those values are not numbers. random includes the choice() function for making a random selection from a sequence. This example simulates flipping a coin 10,000 times to count how many times it comes up heads and how many times tails.

```
# random_choice.py
import random
import itertools

outcomes = {
    "heads": 0,
    "tails": 0,
}
sides = list(outcomes.keys())

for i in range(10000):
    outcomes[random.choice(sides)] += 1

print("Heads:", outcomes["heads"])
print("Tails:", outcomes["tails"])
```

There are only two outcomes allowed, so rather than use numbers and convert them the words “heads” and “tails” are used with choice(). The results are tabulated in a dictionary using the outcome names as keys.

```
$ python3 random_choice.py
Heads: 4986
Tails: 5014
```