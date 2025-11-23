"""
list.copy() (Shallow Copy)
Creates a new list object, but does not copy nested lists.
If the list contains inner lists, they still reference the original inner lists.
"""

import copy

a = [[1,2], [3,4]]
b = a.copy()  # shallow copy
b[0].append(9)

print(a)  # [[1,2,9], [3,4]] → inner list changed!
print(b)  # [[1,2,9], [3,4]]

Deepcopy
 
import copy

a = [[1,2], [3,4]]
b = copy.deepcopy(a)  # deep copy
b[0].append(9)

print(a)  # [[1,2], [3,4]] → original unchanged
print(b)  # [[1,2,9], [3,4]]
