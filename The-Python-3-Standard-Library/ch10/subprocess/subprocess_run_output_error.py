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
