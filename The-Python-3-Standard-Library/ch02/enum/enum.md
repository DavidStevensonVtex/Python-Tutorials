# Chapter 2: Data Structures

## 2.1 enum: Enumeration Type

The enum module defines an enumeration type with iteration and comparison capabilities. It can be used to create well-defined symbols for values, instead of using literal integers or strings.

### 2.1.1 Creating Enumerations

A new enumeration is defined using the class syntax by subclassing Enum and adding class attributes describing the values.

```
# enum_create.py
import enum


class BugStatus(enum.Enum):

    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1


print('\nMember name: {}'.format(BugStatus.wont_fix.name))
print('Member value: {}'.format(BugStatus.wont_fix.value))
```

The members of the Enum are converted to instances as the class is parsed. Each instance has a name property corresponding to the member name and a value property corresponding to the value assigned to the name in the class definition.

```
$ python3 enum_create.py 

Member name: wont_fix
Member value: 4
```

### 2.1.2 Iteration

Iterating over the enum class produces the individual members of the enumeration.

```
# enum_iterate.py

import enum


class BugStatus(enum.Enum):

    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1


for status in BugStatus:
    print('{:15} = {}'.format(status.name, status.value))
```

The members are produced in the order they are declared in the class definition. The names and values are not used to sort them in any way.

```
$ python3 enum_iterate.py 
new             = 7
incomplete      = 6
invalid         = 5
wont_fix        = 4
in_progress     = 3
fix_committed   = 2
fix_released    = 1
```