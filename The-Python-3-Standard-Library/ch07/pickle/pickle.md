# [Chapter 7: Data Persistence and Exchange](https://pymotw.com/3/persistence.html)

## [7.1 pickle — Object Serialization](https://pymotw.com/3/pickle/index.html)

Purpose:	Object serialization

The pickle module implements an algorithm for turning an arbitrary Python object into a series of bytes. This process is also called serializing the object. The byte stream representing the object can then be transmitted or stored, and later reconstructed to create a new object with the same characteristics.

<div style="color: black; background-color:pink">
Warning

The documentation for pickle makes clear that it offers no security guarantees. In fact, unpickling data can execute arbitrary code. Be careful using pickle for inter-process communication or data storage, and do not trust data that cannot be verified as secure. See the hmac module for an example of a secure way to verify the source of a pickled data source.
</div>

