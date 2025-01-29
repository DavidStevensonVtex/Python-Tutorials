# Chapter 2: Data Structures

## [2.3 array — Sequence of Fixed-type Data](https://pymotw.com/3/array/index.html)

Purpose:	Manage sequences of fixed-type numerical data efficiently.

The array module defines a sequence data structure that looks very much like a list, except that all of the members have to be of the same primitive type. The types supported are all numeric or other fixed-size primitive types such as bytes.

Refer to the table below for some of the supported types. The standard library documentation for array includes a complete list of type codes.

Type Codes for array Members

Code	Type	Minimum size (bytes)

* b	int	1
* B	int	1
* h	signed short	2
* H	unsigned short	2
* i	signed int	2
* I	unsigned int	2
* l	signed long	4
* L	unsigned long	4
* q	signed long long	8
* Q	unsigned long long	8
* f	float	4
* d	double float	8