# [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)

[The Python Standard Library](https://docs.python.org/3/library/)

## [12. Virtual Environments and Packages](https://docs.python.org/3/tutorial/venv.html)

### 12.1. Introduction

Python applications will often use packages and modules that don’t come as part of the standard library. Applications will sometimes need a specific version of a library, because the application may require that a particular bug has been fixed or the application may be written using an obsolete version of the library’s interface.

This means it may not be possible for one Python installation to meet the requirements of every application. If application A needs version 1.0 of a particular module but application B needs version 2.0, then the requirements are in conflict and installing either version 1.0 or 2.0 will leave one application unable to run.

The solution for this problem is to create a virtual environment, a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages.

Different applications can then use different virtual environments. To resolve the earlier example of conflicting requirements, application A can have its own virtual environment with version 1.0 installed while application B has another virtual environment with version 2.0. If application B requires a library be upgraded to version 3.0, this will not affect application A’s environment.

### 12.2. Creating Virtual Environments
The module used to create and manage virtual environments is called venv. venv will install the Python version from which the command was run (as reported by the --version option). For instance, executing the command with python3.12 will install version 3.12.

To create a virtual environment, decide upon a directory where you want to place it, and run the venv module as a script with the directory path:

`python -m venv tutorial-env`

```
$ python3 -m venv tutorial-env
The virtual environment was not created successfully because ensurepip is not
available.  On Debian/Ubuntu systems, you need to install the python3-venv
package using the following command.

    apt install python3.8-venv

You may need to use sudo with that command.  After installing the python3-venv
package, recreate your virtual environment.
```

This will create the tutorial-env directory if it doesn’t exist, and also create directories inside it containing a copy of the Python interpreter and various supporting files.

A common directory location for a virtual environment is .venv. This name keeps the directory typically hidden in your shell and thus out of the way while giving it a name that explains why the directory exists. It also prevents clashing with .env environment variable definition files that some tooling supports.
```

`python -m venv tutorial-env`

This will create the tutorial-env directory if it doesn’t exist, and also create directories inside it containing a copy of the Python interpreter and various supporting files.

A common directory location for a virtual environment is .venv. This name keeps the directory typically hidden in your shell and thus out of the way while giving it a name that explains why the directory exists. It also prevents clashing with .env environment variable definition files that some tooling supports.

Once you’ve created a virtual environment, you may activate it.

On Unix or MacOS, run:

```
$ source tutorial-env/bin/activate
(tutorial-env) $ python
Python 3.8.10 (default, Nov  7 2024, 13:10:47) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
`

To deactivate a virtual environment, type:

`deactivate`

into the terminal.