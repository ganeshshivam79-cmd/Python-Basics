from collections import deque

lst = deque([2, 3, 4])
lst.appendleft(1)

print(list(lst))