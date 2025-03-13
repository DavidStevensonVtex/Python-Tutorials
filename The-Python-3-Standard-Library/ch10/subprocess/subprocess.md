# [Chapter 10: Concurrency with Processes, Threads, and Coroutines](https://pymotw.com/3/concurrency.html)

## [10.1 subprocess — Spawning Additional Processes](https://pymotw.com/3/subprocess/index.html)

**Purpose:**	Start and communicate with additional processes.

The subprocess module supports three APIs for working with processes. The run() function, added in Python 3.5, is a high-level API for running a process and optionally collecting its output. The functions call(), check_call(), and check_output() are the former high-level API, carried over from Python 2. They are still supported and widely used in existing programs. The class Popen is a low-level API used to build the other APIs and useful for more complex process interactions. The constructor for Popen takes arguments to set up the new process so the parent can communicate with it via pipes. It provides all of the functionality of the other modules and functions it replaces, and more. The API is consistent for all uses, and many of the extra steps of overhead needed (such as closing extra file descriptors and ensuring the pipes are closed) are “built in” instead of being handled by the application code separately.

The subprocess module is intended to replace functions such as os.system(), os.spawnv(), the variations of popen() in the os and popen2 modules, as well as the commands() module. To make it easier to compare subprocess with those other modules, many of the examples in this section re-create the ones used for os and popen2.

Note

The API for working on Unix and Windows is roughly the same, but the underlying implementation is different because of the difference in process models in the operating systems. All of the examples shown here were tested on Mac OS X. Behavior on a non-Unix OS may vary.

### 10.1.1 Running External Command

To run an external command without interacting with it in the same way as os.system(), use the run() function.

```
# subprocess_os_system.py
import subprocess

completed = subprocess.run(["ls", "-1"])
print("returncode:", completed.returncode)
```

The command line arguments are passed as a list of strings, which avoids the need for escaping quotes or other special characters that might be interpreted by the shell. run() returns a CompletedProcess instance, with information about the process like the exit code and output.

```
$ python3 subprocess_os_system.py
subprocess.md
subprocess_os_system.py
returncode: 0
```

Setting the shell argument to a true value causes subprocess to spawn an intermediate shell process which then runs the command. The default is to run the command directly.

```
# subprocess_shell_variables.py
import subprocess

completed = subprocess.run("echo $HOME", shell=True)
print("returncode:", completed.returncode)
```

Using an intermediate shell means that variables, glob patterns, and other special shell features in the command string are processed before the command is run.

```
$ python3 subprocess_shell_variables.py
/home/dstevenson
returncode: 0
```

Note

Using run() without passing check=True is equivalent to using call(), which only returned the exit code from the process.

#### 10.1.1.1 Error Handling

The returncode attribute of the CompletedProcess is the exit code of the program. The caller is responsible for interpreting it to detect errors. If the check argument to run() is True, the exit code is checked and if it indicates an error happened then a CalledProcessError exception is raised.

```
# subprocess_run_check.py
import subprocess

try:
    subprocess.run(["false"], check=True)
except subprocess.CalledProcessError as err:
    print("ERROR:", err)
```

The false command always exits with a non-zero status code, which run() interprets as an error.

```
$ python3 subprocess_run_check.py
ERROR: Command '['false']' returned non-zero exit status 1.
```

Note

Passing check=True to run() makes it equivalent to using check_call().

#### 10.1.1.2 Capturing Output

The standard input and output channels for the process started by run() are bound to the parent’s input and output. That means the calling program cannot capture the output of the command. Pass PIPE for the stdout and stderr arguments to capture the output for later processing.

```
# subprocess_run_output.py
import subprocess

completed = subprocess.run(
    ["ls", "-1"],
    stdout=subprocess.PIPE,
)
print("returncode:", completed.returncode)
print(
    "Have {} bytes in stdout:\n{}".format(
        len(completed.stdout), completed.stdout.decode("utf-8")
    )
)
```

The ls -1 command runs successfully, so the text it prints to standard output is captured and returned.

```
$ python3 subprocess_run_output.py
returncode: 0
Have 117 bytes in stdout:
subprocess.md
subprocess_os_system.py
subprocess_run_check.py
subprocess_run_output.py
subprocess_shell_variables.py
```

Note

Passing check=True and setting stdout to PIPE is equivalent to using check_output().

The next example runs a series of commands in a sub-shell. Messages are sent to standard output and standard error before the commands exit with an error code.

```
# subprocess_run_output_error.py
import subprocess

try:
    completed = subprocess.run(
        "echo to stdout; echo to stderr 1>&2; exit 1",
        check=True,
        shell=True,
        stdout=subprocess.PIPE,
    )
except subprocess.CalledProcessError as err:
    print("ERROR:", err)
else:
    print("returncode:", completed.returncode)
    print(
        "Have {} bytes in stdout: {!r}".format(
            len(completed.stdout), completed.stdout.decode("utf-8")
        )
    )
```

The message to standard error is printed to the console, but the message to standard output is hidden.

```
$ python3 subprocess_run_output_error.py
to stderr
ERROR: Command 'echo to stdout; echo to stderr 1>&2; exit 1' returned non-zero exit status 1.
```

To prevent error messages from commands run through run() from being written to the console, set the stderr parameter to the constant PIPE.

```
# subprocess_run_output_error_trap.py
import subprocess

try:
    completed = subprocess.run(
        'echo to stdout; echo to stderr 1>&2; exit 1',
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
except subprocess.CalledProcessError as err:
    print('ERROR:', err)
else:
    print('returncode:', completed.returncode)
    print('Have {} bytes in stdout: {!r}'.format(
        len(completed.stdout),
        completed.stdout.decode('utf-8'))
    )
    print('Have {} bytes in stderr: {!r}'.format(
        len(completed.stderr),
        completed.stderr.decode('utf-8'))
    )
```

This example does not set check=True so the output of the command is captured and printed.

```
$ python3 subprocess_run_output_error_trap.py
returncode: 1
Have 10 bytes in stdout: 'to stdout\n'
Have 10 bytes in stderr: 'to stderr\n'
```

To capture error messages when using check_output(), set stderr to STDOUT, and the messages will be merged with the rest of the output from the command.

```
# subprocess_check_output_error_trap_output.py
import subprocess

try:
    output = subprocess.check_output(
        "echo to stdout; echo to stderr 1>&2",
        shell=True,
        stderr=subprocess.STDOUT,
    )
except subprocess.CalledProcessError as err:
    print("ERROR:", err)
else:
    print("Have {} bytes in output: {!r}".format(len(output), output.decode("utf-8")))
```

The order of output may vary, depending on how buffering is applied to the standard output stream and how much data is being printed.

```
$ python3 subprocess_check_output_error_trap_output.py
Have 20 bytes in output: 'to stdout\nto stderr\n'
```

#### 10.1.1.3 Suppressing Output

For cases where the output should not be shown or captured, use DEVNULL to suppress an output stream. This example suppresses both the standard output and error streams.

```
# subprocess_run_output_error_suppress.py
import subprocess

try:
    completed = subprocess.run(
        "echo to stdout; echo to stderr 1>&2; exit 1",
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
except subprocess.CalledProcessError as err:
    print("ERROR:", err)
else:
    print("returncode:", completed.returncode)
    print("stdout is {!r}".format(completed.stdout))
    print("stderr is {!r}".format(completed.stderr))
```

The name DEVNULL comes from the Unix special device file, /dev/null, which responds with end-of-file when opened for reading and receives but ignores any amount of input when writing.

```
$ python3 subprocess_run_output_error_suppress.py
returncode: 1
stdout is None
stderr is None
```