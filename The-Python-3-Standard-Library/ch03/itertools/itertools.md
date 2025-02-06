# [Chapter 3 Algorithms](https://pymotw.com/3/algorithm_tools.html)

## [3.2 itertools — Iterator Functions](https://pymotw.com/3/itertools/index.html)

Purpose:	The itertools module includes a set of functions for working with sequence data sets.

The functions provided by itertools are inspired by similar features of functional programming languages such as Clojure, Haskell, APL, and SML. They are intended to be fast and use memory efficiently, and also to be hooked together to express more complicated iteration-based algorithms.

Iterator-based code offers better memory consumption characteristics than code that uses lists. Since data is not produced from the iterator until it is needed, all of the data does not need to be stored in memory at the same time. This “lazy” processing model can reduce swapping and other side-effects of large data sets, improving performance.

In addition to the functions defined in itertools, the examples in this section also rely on some of the built-in functions for iteration.