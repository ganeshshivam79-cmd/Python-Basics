import pandas as pd
s = pd.Series(['cat', 'dog'])
print(s.str.pad(6, fillchar='*', side='right'))


#namedtuple is a function from Python’s collections module
#that lets you create tuple-like objects with named fields — making your code more
#readable and self-documenting.
from collections import namedtuple

Person = namedtuple("Person", ["name", "age", "city"])
p = Person(name="Alice", age=30, city="New York")

print(p.name)   # Alice
print(p.age)    # 30
print(p[2])     # New York (also accessible like a regular tuple)
print(Person._fields)
#namedtuple is immutable

from collections import defaultdict
d = defaultdict(int)
d["apple"] += 1
d["banana"] += 1
print(d)  # Output: defaultdict(<class 'int'>, {'apple': 1, 'banana': 1})


from collections import deque
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print(dq)  # Output: deque([0, 1, 2, 3, 4])

from collections import OrderedDict

od = OrderedDict()
od["one"] = 1
od["two"] = 2
print(od)  # Output: OrderedDict([('one', 1), ('two', 2)])
