# [Chapter 6: The File System](https://pymotw.com/3/file_access.html)

## [6.9 mmap — Memory-map Files](https://pymotw.com/3/mmap/index.html)

Purpose:	Memory-map files instead of reading the contents directly.

Memory-mapping a file uses the operating system virtual memory system to access the data on the file system directly, instead of using normal I/O functions. Memory-mapping typically improves I/O performance because it does not involve a separate system call for each access and it does not require copying data between buffers – the memory is accessed directly by both the kernel and the user application.

Memory-mapped files can be treated as mutable strings or file-like objects, depending on the need. A mapped file supports the expected file API methods, such as close(), flush(), read(), readline(), seek(), tell(), and write(). It also supports the string API, with features such as slicing and methods like find().

All of the examples use the text file lorem.txt, containing a bit of Lorem Ipsum. For reference, the text of the file is

```
# lorem.txt
Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
Donec egestas, enim et consectetuer ullamcorper, lectus ligula rutrum leo,
a elementum elit tortor eu quam. Duis tincidunt nisi ut ante. Nulla
facilisi. Sed tristique eros eu libero. Pellentesque vel
arcu. Vivamus purus orci, iaculis ac, suscipit sit amet, pulvinar eu,
lacus. Praesent placerat tortor sed nisl. Nunc blandit diam egestas
dui. Pellentesque habitant morbi tristique senectus et netus et
malesuada fames ac turpis egestas. Aliquam viverra fringilla
leo. Nulla feugiat augue eleifend nulla. Vivamus mauris. Vivamus sed
mauris in nibh placerat egestas. Suspendisse potenti. Mauris
massa. Ut eget velit auctor tortor blandit sollicitudin. Suspendisse
imperdiet justo.
```

Note

There are differences in the arguments and behaviors for mmap() between Unix and Windows, which are not fully discussed here. For more details, refer to the standard library documentation.

