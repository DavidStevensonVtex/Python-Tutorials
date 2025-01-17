# string_template.py
import string

values = {'var': 'foo'}

t = string.Template("""
Variable        : $var
Escape          : $$
Variable in text: ${var}iable
""")

print('TEMPLATE:', t.substitute(values))

s = """
Variable        : %(var)s
Escape          : %%
Variable in text: %(var)siable
"""

print('INTERPOLATION:', s % values)

s = """
Variable        : {var}
Escape          : {{}}
Variable in text: {var}iable
"""

print('FORMAT:', s.format(**values))

# $ python3 string_templates.py 
# TEMPLATE: 
# Variable        : foo
# Escape          : $
# Variable in text: fooiable

# INTERPOLATION: 
# Variable        : foo
# Escape          : %
# Variable in text: fooiable

# FORMAT: 
# Variable        : foo
# Escape          : {}
# Variable in text: fooiable