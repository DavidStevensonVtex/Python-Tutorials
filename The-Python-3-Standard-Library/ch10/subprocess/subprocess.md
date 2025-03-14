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

### 10.1.2 Working with Pipes Directly

The functions run(), call(), check_call(), and check_output() are wrappers around the Popen class. Using Popen directly gives more control over how the command is run, and how its input and output streams are processed. For example, by passing different arguments for stdin, stdout, and stderr it is possible to mimic the variations of os.popen().

#### 10.1.2.1 One-way Communication With a Process

To run a process and read all of its output, set the stdout value to PIPE and call communicate().

```
# subprocess_popen_read.py
import subprocess

print("read:")
proc = subprocess.Popen(
    ["echo", '"to stdout"'],
    stdout=subprocess.PIPE,
)
stdout_value = proc.communicate()[0].decode("utf-8")
print("stdout:", repr(stdout_value))
```

This is similar to the way popen() works, except that the reading is managed internally by the Popen instance.

```
$ python3 subprocess_popen_read.py
read:
stdout: '"to stdout"\n'
```

To set up a pipe to allow the calling program to write data to it, set stdin to PIPE.

```
# subprocess_popen_write.py
import subprocess

print("write:")
proc = subprocess.Popen(
    ["cat", "-"],
    stdin=subprocess.PIPE,
)
proc.communicate("stdin: to stdin\n".encode("utf-8"))
```

To send data to the standard input channel of the process one time, pass the data to communicate(). This is similar to using popen() with mode 'w'.

```
$ python3 -u subprocess_popen_write.py
write:
stdin: to stdin
```

#### 10.1.2.2 Bi-directional Communication With a Process

To set up the Popen instance for reading and writing at the same time, use a combination of the previous techniques.

```
# subprocess_popen2.py
import subprocess

print("popen2:")

proc = subprocess.Popen(
    ["cat", "-"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
)
msg = "through stdin to stdout".encode("utf-8")
stdout_value = proc.communicate(msg)[0].decode("utf-8")
print("pass through:", repr(stdout_value))
```

This sets up the pipe to mimic popen2().

The "-u" option forces unbuffered output for standard output and error.

```
-u     : force the stdout and stderr streams to be unbuffered;
         this option has no effect on stdin; also PYTHONUNBUFFERED=x
```

```
$ python3 -u subprocess_popen2.py
popen2:
pass through: 'through stdin to stdout'
```

#### 10.1.2.3 Capturing Error Output

It is also possible watch both of the streams for stdout and stderr, as with popen3().

```
# subprocess_popen3.py
import subprocess

print("popen3:")
proc = subprocess.Popen(
    'cat -; echo "to stderr" 1>&2',
    shell=True,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)
msg = "through stdin to stdout".encode("utf-8")
stdout_value, stderr_value = proc.communicate(msg)
print("pass through:", repr(stdout_value.decode("utf-8")))
print("stderr      :", repr(stderr_value.decode("utf-8")))
```

Reading from stderr works the same as with stdout. Passing PIPE tells Popen to attach to the channel, and communicate() reads all of the data from it before returning.

```
$ python3 -u subprocess_popen3.py
popen3:
pass through: 'through stdin to stdout'
stderr      : 'to stderr\n'
```

#### 10.1.2.4 Combining Regular and Error Output

To direct the error output from the process to its standard output channel, use STDOUT for stderr instead of PIPE.

```
# subprocess_popen4.py
import subprocess

print("popen4:")
proc = subprocess.Popen(
    'cat -; echo "to stderr" 1>&2',
    shell=True,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
)
msg = "through stdin to stdout\n".encode("utf-8")
stdout_value, stderr_value = proc.communicate(msg)
print("combined output:", repr(stdout_value.decode("utf-8")))
print("stderr value   :", repr(stderr_value))
```

Combining the output in this way is similar to how popen4() works.

```
$ python3 -u subprocess_popen4.py
popen4:
combined output: 'through stdin to stdout\nto stderr\n'
stderr value   : None
```

### 10.1.3 Connecting Segments of a Pipe

Multiple commands can be connected into a pipeline, similar to the way the Unix shell works, by creating separate Popen instances and chaining their inputs and outputs together. The stdout attribute of one Popen instance is used as the stdin argument for the next in the pipeline, instead of the constant PIPE. The output is read from the stdout handle for the final command in the pipeline.

```
# subprocess_pipes.py
import subprocess

cat = subprocess.Popen(
    ["cat", "index.rst"],
    stdout=subprocess.PIPE,
)

grep = subprocess.Popen(
    ["grep", ".. literalinclude"],
    stdin=cat.stdout,
    stdout=subprocess.PIPE,
)

cut = subprocess.Popen(
    ["cut", "-f", "3", "-d:"],
    stdin=grep.stdout,
    stdout=subprocess.PIPE,
)

end_of_pipe = cut.stdout

print("Included files:")
for line in end_of_pipe:
    print(line.decode("utf-8").strip())
```

The example reproduces the command line:

`$ cat index.rst | grep ".. literalinclude" | cut -f 3 -d:`

The pipeline reads the reStructuredText source file for this section and finds all of the lines that include other files, then prints the names of the files being included.

```
python3 -u subprocess_pipes.py
```

### 10.1.4 Interacting with Another Command

All of the previous examples assume a limited amount of interaction. The communicate() method reads all of the output and waits for child process to exit before returning. It is also possible to write to and read from the individual pipe handles used by the Popen instance incrementally, as the program runs. A simple echo program that reads from standard input and writes to standard output illustrates this technique.

The script repeater.py is used as the child process in the next example. It reads from stdin and writes the values to stdout, one line at a time until there is no more input. It also writes a message to stderr when it starts and stops, showing the lifetime of the child process.

```
# repeater.py
import sys

sys.stderr.write("repeater.py: starting\n")
sys.stderr.flush()

while True:
    next_line = sys.stdin.readline()
    sys.stderr.flush()
    if not next_line:
        break
    sys.stdout.write(next_line)
    sys.stdout.flush()

sys.stderr.write("repeater.py: exiting\n")
sys.stderr.flush()
```

The next interaction example uses the stdin and stdout file handles owned by the Popen instance in different ways. In the first example, a sequence of five numbers are written to stdin of the process, and after each write the next line of output is read back. In the second example, the same five numbers are written but the output is read all at once using communicate().

```
# interaction.py
import io
import subprocess

print("One line at a time:")
proc = subprocess.Popen(
    "python3 repeater.py",
    shell=True,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
)
stdin = io.TextIOWrapper(
    proc.stdin,
    encoding="utf-8",
    line_buffering=True,  # send data on newline
)
stdout = io.TextIOWrapper(
    proc.stdout,
    encoding="utf-8",
)
for i in range(5):
    line = "{}\n".format(i)
    stdin.write(line)
    output = stdout.readline()
    print(output.rstrip())
remainder = proc.communicate()[0].decode("utf-8")
print(remainder)

print()
print("All output at once:")
proc = subprocess.Popen(
    "python3 repeater.py",
    shell=True,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
)
stdin = io.TextIOWrapper(
    proc.stdin,
    encoding="utf-8",
)
for i in range(5):
    line = "{}\n".format(i)
    stdin.write(line)
stdin.flush()

output = proc.communicate()[0].decode("utf-8")
print(output)
```

The "repeater.py: exiting" lines come at different points in the output for each loop style.

```
$ python3 -u interaction.py
One line at a time:
repeater.py: starting
0
1
2
3
4
repeater.py: exiting


All output at once:
repeater.py: starting
repeater.py: exiting
0
1
2
3
4
```

### 10.1.5 Signaling Between Processes

The process management examples for the os module include a demonstration of signaling between processes using os.fork() and os.kill(). Since each Popen instance provides a pid attribute with the process id of the child process, it is possible to do something similar with subprocess. The next example combines two scripts. This child process sets up a signal handler for the USR signal.

```
# signal_child.py
import os
import signal
import time
import sys

pid = os.getpid()
received = False


def signal_usr1(signum, frame):
    "Callback invoked when a signal is received"
    global received
    received = True
    print("CHILD {:>6}: Received USR1".format(pid))
    sys.stdout.flush()


print("CHILD {:>6}: Setting up signal handler".format(pid))
sys.stdout.flush()
signal.signal(signal.SIGUSR1, signal_usr1)
print("CHILD {:>6}: Pausing to wait for signal".format(pid))
sys.stdout.flush()
time.sleep(3)

if not received:
    print("CHILD {:>6}: Never received signal".format(pid))
```

This script runs as the parent process. It starts signal_child.py, then sends the USR1 signal.

```
# signal_parent.py
import os
import signal
import subprocess
import time
import sys

proc = subprocess.Popen(["python3", "signal_child.py"])
print("PARENT      : Pausing before sending signal...")
sys.stdout.flush()
time.sleep(1)
print("PARENT      : Signaling child")
sys.stdout.flush()
os.kill(proc.pid, signal.SIGUSR1)
```

The output is:

```
$ python3 signal_parent.py
PARENT      : Pausing before sending signal...
CHILD  19972: Setting up signal handler
CHILD  19972: Pausing to wait for signal
PARENT      : Signaling child
CHILD  19972: Received USR1
```