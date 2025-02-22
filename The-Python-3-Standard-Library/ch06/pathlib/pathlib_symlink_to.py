# pathlib_symlink_to.py
import pathlib

p = pathlib.Path("example_link")

p.symlink_to("pathlib.md")

print(p)
print(p.resolve().name)
