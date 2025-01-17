# string_template_advanced.py
import string


class MyTemplate(string.Template):
    delimiter = '%'
    idpattern = '[a-z]+_[a-z]+'


template_text = '''
  Delimiter : %%
  Replaced  : %with_underscore
  Ignored   : %notunderscored
'''

d = {
    'with_underscore': 'replaced',
    'notunderscored': 'not replaced',
}

t = MyTemplate(template_text)
print('Modified ID pattern:')
print(t.safe_substitute(d))

# $ python3 string_template_advanced.py
# Modified ID pattern:

#   Delimiter : %
#   Replaced  : replaced
#   Ignored   : %notunderscored
