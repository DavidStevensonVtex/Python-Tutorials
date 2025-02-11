# contextlib_exitstack_enter_context_errors.py

import contextlib
from contextlib_context_managers import *


def variable_stack(tests):
    with contextlib.ExitStack() as stack:
        for test in tests:
            stack.enter_context(test)
    print("  outside of stack, any errors were handled")


# The examples using these classes are based around variable_stack(), which uses the
# context managers passed to construct an ExitStack, building up the overall context
# one by one. The examples below pass different context managers to explore the error
# handling behavior. First, the normal case of no exceptions.

print("No errors:")
variable_stack(
    [
        HandleError(1),
        PassError(2),
    ]
)

# Then, an example of handling exceptions within the context managers at the end of the stack,
# in which all of the open contexts are closed as the stack is unwound.

print("\nError at the end of the context stack:")
variable_stack(
    [
        HandleError(1),
        HandleError(2),
        ErrorOnExit(3),
    ]
)

# Next, an example of handling exceptions within the context managers in the middle of the stack,
# in which the error does not occur until some contexts are already closed, so those contexts do
# not see the error.

print("\nError in the middle of the context stack:")
variable_stack(
    [
        HandleError(1),
        PassError(2),
        ErrorOnExit(3),
        HandleError(4),
    ]
)

# Finally, an example of the exception remaining unhandled and propagating up to the calling code.

try:
    print("\nError ignored:")
    variable_stack(
        [
            PassError(1),
            ErrorOnExit(2),
        ]
    )
except RuntimeError:
    print("error handled outside of context")
