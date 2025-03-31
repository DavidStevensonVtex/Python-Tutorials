# Python for Data Science for Dummies, 3rd Edition, © 2024

## Chapter 5: Working with Jupyter Notebook

### Using Jupyter Notebook The Jupyter Notebook Integrated Development Environment (IDE) is part of the Anaconda suite of tools.

#### Working with Styles

You can use Notebook to create sections and add styles so that the output is nicely formatted. What you end up with is a good-looking report that just happens to contain executable code.

The default style for a cell is Code. However, when you click the down arrow next to the Code entry, you see a listing of styles.

* Code
* Markdown
* [Raw NBConvert](https://nbconvert.readthedocs.io/en/latest/)
* Heading

The goal of the Raw NBConvert style is to allow you to include special content, such as Lamport TeX (LaTeX) content. The LaTeX document system isn't tied to a particular editor -- it's simply a means of encoding scientific documents.

#### Getting Python Help

To obtain help, select one of the entries on the Help menu.
* [Notebook Help](https://nbviewer.org/github/ipython/ipython/blob/3.x/examples/Notebook/Index.ipynb)
* [Markdown] (https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github)
* [Python Reference](https://docs.python.org/3.10/)
* [IPython Reference](https://ipython.org/documentation.html)
* [NumPy Reference](https://numpy.org/doc/stable/reference/)
* [SciPy Reference](https://docs.scipy.org/doc/scipy/reference/)
* [Matplotlib Reference](https://matplotlib.org/stable/users/)
* [SymPy Reference](https://docs.sympy.org/latest/index.html?v=20250329181059)
* [pandas Reference](https://pandas.pydata.org/pandas-docs/stable/)

#### Using magic functions

Jupyter provides a special feature called magic functions.

##### Obtaining the magic functions list

The best way to start working with magic functions is to obtain a list of them by typing `%quickref` and pressing enter.

```
IPython -- An enhanced Interactive Python - Quick Reference Card
================================================================

obj?, obj??      : Get help, or more help for object (also works as
                   ?obj, ??obj).
?foo.*abc*       : List names in 'foo' containing 'abc' in them.
%magic           : Information about IPython's 'magic' % functions.

Magic functions are prefixed by % or %%, and typically take their arguments
without parentheses, quotes or even commas for convenience.  Line magics take a
single % and cell magics are prefixed with two %%.

Example magic function calls:

%alias d ls -F   : 'd' is now an alias for 'ls -F'
alias d ls -F    : Works if 'alias' not a python name
alist = %alias   : Get list of aliases to 'alist'
cd /usr/share    : Obvious. cd -<tab> to choose from visited dirs.
%cd??            : See help AND source for magic %cd
%timeit x=10     : time the 'x=10' statement with high precision.
%%timeit x=2**100
x**100           : time 'x**100' with a setup of 'x=2**100'; setup code is not
                   counted.  This is an example of a cell magic.

System commands:

!cp a.txt b/     : System command escape, calls os.system()
cp a.txt b/      : after %rehashx, most system commands work without !
cp ${f}.txt $bar : Variable expansion in magics and system commands
files = !ls /usr : Capture system command output
files.s, files.l, files.n: "a b c", ['a','b','c'], 'a\nb\nc'

History:

_i, _ii, _iii    : Previous, next previous, next next previous input
_i4, _ih[2:5]    : Input history line 4, lines 2-4
exec(_i81)       : Execute input history line #81 again
%rep 81          : Edit input history line #81
_, __, ___       : previous, next previous, next next previous output
_dh              : Directory history
_oh              : Output history
%hist            : Command history of current session.
%hist -g foo     : Search command history of (almost) all sessions for 'foo'.
%hist -g         : Command history of (almost) all sessions.
%hist 1/2-8      : Command history containing lines 2-8 of session 1.
%hist 1/ ~2/     : Command history of session 1 and 2 sessions before current.
%hist ~8/1-~6/5  : Command history from line 1 of 8 sessions ago to
                   line 5 of 6 sessions ago.
%edit 0/         : Open editor to execute code with history of current session.

Autocall:

f 1,2            : f(1,2)  # Off by default, enable with %autocall magic.
/f 1,2           : f(1,2) (forced autoparen)
,f 1 2           : f("1","2")
;f 1 2           : f("1 2")

Remember: TAB completion works in many contexts, not just file names
or python names.

The following magic functions are currently available:

%alias:
    Define an alias for a system command.
%alias_magic:
    ::
%autoawait:
    
%autocall:
    Make functions callable without having to type parentheses.
%automagic:
    Make magic functions callable without having to type the initial %.
%autosave:
    Set the autosave interval in the notebook (in seconds).
%bookmark:
    Manage IPython's bookmark system.
%cat:
    Alias for `!cat`
%cd:
    Change the current working directory.
%clear:
    Clear the terminal.
%colors:
    Switch color scheme for prompts, info system and exception handlers.
%conda:
    Run the conda package manager within the current kernel.
%config:
    configure IPython
%connect_info:
    Print information for connecting other clients to this kernel
%cp:
    Alias for `!cp`
%debug:
    ::
%dhist:
    Print your history of visited directories.
%dirs:
    Return the current directory stack.
%doctest_mode:
    Toggle doctest mode on and off.
%ed:
    Alias for `%edit`.
%edit:
    Bring up an editor and execute the resulting code.
%env:
    Get, set, or list environment variables.
%gui:
    Enable or disable IPython GUI event loop integration.
%hist:
    Alias for `%history`.
%history:
    ::
%killbgscripts:
    Kill all BG processes started by %%script and its family.
%ldir:
    Alias for `!ls -F -o --color %l | grep /$`
%less:
    Show a file through the pager.
%lf:
    Alias for `!ls -F -o --color %l | grep ^-`
%lk:
    Alias for `!ls -F -o --color %l | grep ^l`
%ll:
    Alias for `!ls -F -o --color`
%load:
    Load code into the current frontend.
%load_ext:
    Load an IPython extension by its module name.
%loadpy:
    Alias of `%load`
%logoff:
    Temporarily stop logging.
%logon:
    Restart logging.
%logstart:
    Start logging anywhere in a session.
%logstate:
    Print the status of the logging system.
%logstop:
    Fully stop logging and close log file.
%ls:
    Alias for `!ls -F --color`
%lsmagic:
    List currently available magic functions.
%lx:
    Alias for `!ls -F -o --color %l | grep ^-..x`
%macro:
    Define a macro for future re-execution. It accepts ranges of history,
%magic:
    Print information about the magic function system.
%man:
    Find the man page for the given command and display in pager.
%matplotlib:
    ::
%mkdir:
    Alias for `!mkdir`
%more:
    Show a file through the pager.
%mv:
    Alias for `!mv`
%notebook:
    ::
%page:
    Pretty print the object and display it through a pager.
%pastebin:
    Upload code to dpaste.com, returning the URL.
%pdb:
    Control the automatic calling of the pdb interactive debugger.
%pdef:
    Print the call signature for any callable object.
%pdoc:
    Print the docstring for an object.
%pfile:
    Print (or run through pager) the file where an object is defined.
%pinfo:
    Provide detailed information about an object.
%pinfo2:
    Provide extra detailed information about an object.
%pip:
    Run the pip package manager within the current kernel.
%popd:
    Change to directory popped off the top of the stack.
%pprint:
    Toggle pretty printing on/off.
%precision:
    Set floating point precision for pretty printing.
%prun:
    Run a statement through the python code profiler.
%psearch:
    Search for object in namespaces by wildcard.
%psource:
    Print (or run through pager) the source code for an object.
%pushd:
    Place the current dir on stack and change directory.
%pwd:
    Return the current working directory path.
%pycat:
    Show a syntax-highlighted file through a pager.
%pylab:
    ::
%qtconsole:
    Open a qtconsole connected to this kernel.
%quickref:
    Show a quick reference sheet 
%recall:
    Repeat a command, or get command to input line for editing.
%rehashx:
    Update the alias table with all executable files in $PATH.
%reload_ext:
    Reload an IPython extension by its module name.
%rep:
    Alias for `%recall`.
%rerun:
    Re-run previous input
%reset:
    Resets the namespace by removing all names defined by the user, if
%reset_selective:
    Resets the namespace by removing names defined by the user.
%rm:
    Alias for `!rm`
%rmdir:
    Alias for `!rmdir`
%run:
    Run the named file inside IPython as a program.
%save:
    Save a set of lines or a macro to a given filename.
%sc:
    Shell capture - run shell command and capture output (DEPRECATED use !).
%set_env:
    Set environment variables.  Assumptions are that either "val" is a
%store:
    Lightweight persistence for python variables.
%sx:
    Shell execute - run shell command and capture output (!! is short-hand).
%system:
    Shell execute - run shell command and capture output (!! is short-hand).
%tb:
    Print the last traceback.
%time:
    Time execution of a Python statement or expression.
%timeit:
    Time execution of a Python statement or expression
%unalias:
    Remove an alias
%unload_ext:
    Unload an IPython extension by its module name.
%who:
    Print all interactive variables, with some minimal formatting.
%who_ls:
    Return a sorted list of all interactive variables.
%whos:
    Like %who, but gives some extra information about each variable.
%xdel:
    Delete a variable, trying to clear it from anywhere that
%xmode:
    Switch modes for the exception handlers.
%%!:
    Shell execute - run shell command and capture output (!! is short-hand).
%%HTML:
    Alias for `%%html`.
%%SVG:
    Alias for `%%svg`.
%%bash:
    %%bash script magic
%%capture:
    ::
%%debug:
    ::
%%file:
    Alias for `%%writefile`.
%%html:
    ::
%%javascript:
    Run the cell block of Javascript code
%%js:
    Run the cell block of Javascript code
%%latex:
    Render the cell as a block of LaTeX
%%markdown:
    Render the cell as Markdown text block
%%perl:
    %%perl script magic
%%prun:
    Run a statement through the python code profiler.
%%pypy:
    %%pypy script magic
%%python:
    %%python script magic
%%python2:
    %%python2 script magic
%%python3:
    %%python3 script magic
%%ruby:
    %%ruby script magic
%%script:
    ::
%%sh:
    %%sh script magic
%%svg:
    Render the cell as an SVG literal
%%sx:
    Shell execute - run shell command and capture output (!! is short-hand).
%%system:
    Shell execute - run shell command and capture output (!! is short-hand).
%%time:
    Time execution of a Python statement or expression.
%%timeit:
    Time execution of a Python statement or expression
%%writefile:
    ::
```

##### Working with magic functions

Most magic functions start with either a single percent sign (%) or two percent signs (%%).
Those with a single percent sign work at the command-line level, and the ones with two percent signs work at the cell level. You generally use magic functions with a single percent sign.

To change directories, you type `%cd <new-directory>`.

#### Discovering Objects

It's a good idea to know how to discover what object you're workign with and what features it provides.

##### Getting object help

You can request information about specific objects using the object name and a question mark (?).

Enter the following Python code into a Code cell in a Jupyter Notebook.

```
mylist = ["apple", "banana", "cherry"]
mylist?
```

```
Type:        list
String form: ['apple', 'banana', 'cherry']
Length:      3
Docstring:  
Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.
```

When you need detailed help about `mylist`, you type `help(mylist)` and click Run.

```
help(mylist)
```

```
Help on list object:

class list(object)
 |  list(iterable=(), /)
 |  
 |  Built-in mutable sequence.
 |  
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(self, /)
 |      Return a reverse iterator over the list.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the list in memory, in bytes.
 |  
 |  append(self, object, /)
 |      Append object to the end of the list.
 |  
 |  clear(self, /)
 |      Remove all items from list.
 |  
 |  copy(self, /)
 |      Return a shallow copy of the list.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.
 |  
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  insert(self, index, object, /)
 |      Insert object before index.
 |  
 |  pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |      
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(self, value, /)
 |      Remove first occurrence of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(self, /)
 |      Reverse *IN PLACE*.
 |  
 |  sort(self, /, *, key=None, reverse=False)
 |      Sort the list in ascending order and return None.
 |      
 |      The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
 |      order of two equal elements is maintained).
 |      
 |      If a key function is given, apply it once to each list item and sort them,
 |      ascending or descending, according to their function values.
 |      
 |      The reverse flag can be set to sort in descending order.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  __class_getitem__(...) from builtins.type
 |      See PEP 585
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None
```

##### Obtaining object specifics

The `dir()` function is often overlooked, but it's an essential way to learn about object specifics.
Use `dir(<object-name>)`.

##### Using extended Python object help

Using a single question mark causes Python to clip long content. If you want to obtain the full content for an object, you need to use the double question mark (??).

`mylist??`

#### Restarting the kernel

Every time you perform a task in your notebook, you create variables, import modules, and perform a wealth of other tasks that modify the environemtn. At some point, you can't really be sure that something is working as it should. To overcome this problem, you save your document by clicking Save and Checkpoint (the button containing a floppy disk symbol), and then click Restart Kernel (the button with an open circle with an arrow at one end).

Whenever you click Restart Kernel, you see a warning message. Make sure to pay attention to the warning because you could lose temporary changes during a kernel restart. Always save your document before you restart the kernel.

#### Restoring a checkpoint

At some point, you may find that you made a mistake. Notebook is notably missing an Undo button: You won't find one anywhere. Instead, you create checkpoints each time you finish a tas. Creating checkpoints when your document is stable and workign properly helps you recover faster from mistakes.

To restore your setup to the condition contained in a checkpoint, choose File-> Revert to Checkpoint. You see a listing of available checkpoints. Simply select the one you want to use. When you select the checkpoint, you see a warning message. When you click Revert, any old information is gone and the information found in the checkpoint becomes the current information.

### Performing Multimedia and Graphic Integration

Pictures say a lot of things that words can't say (or at least they do it with far less effort). Notebook is both a coding platform and presentation platform.
