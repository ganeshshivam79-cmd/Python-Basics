Operator Overloading
__eq__ → for ==
__add__ → for +
__mul__ → for *
__lt__ → for <
__gt__ → for >


#########################################| Method     | Purpose     |
| ---------- | ----------- |
| `__init__` | constructor |
| `__del__`  | destructor  |

#############################################
Container behavior

| Method        | Purpose          |
| ------------- | ---------------- |
| `__getitem__` | obj[key]         |
| `__setitem__` | obj[key] = value |
| `__delitem__` | del obj[key]     |
| `__len__`     | len(obj)         |


#############################################
Attribute Access Methods

| Method        | Purpose                         |
| ------------- | ------------------------------- |
| `__getattr__` | called when attribute not found |
| `__setattr__` | runs on every attribute set     |
| `__delattr__` | runs on deleting an attribute   |

#############################################
Context Manager Methods
| Method      | Purpose          |
| ----------- | ---------------- |
| `__enter__` | start of context |
| `__exit__`  | end of context   |

#############################################
Inheritance Types

Not method types but part of OOP:

Single inheritance
Multiple inheritance
Multilevel inheritance
Hierarchical inheritance
Hybrid inheritance