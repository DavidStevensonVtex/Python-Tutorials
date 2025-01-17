# string_template_defaultpattern.py
import string

t = string.Template('$var')
print(t.pattern.pattern)

# $ python3 string_template_defaultpattern.py 

#     \$(?:
#       (?P<escaped>\$) |   # Escape sequence of two delimiters
#       (?P<named>(?a:[_a-z][_a-z0-9]*))      |   # delimiter and a Python identifier
#       {(?P<braced>(?a:[_a-z][_a-z0-9]*))}  |   # delimiter and a braced identifier
#       (?P<invalid>)              # Other ill-formed delimiter exprs
#     )
    