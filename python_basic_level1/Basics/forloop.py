

for i in range(10, 0 ,-2):
    print(i)

for i in range(0, 10 ,2):
    print(i)

nums = [1, 2, 3, 4, 5]
for i in reversed(nums):
    print(i)


pairs = [(i, j) for i in range(3) for j in range(3)]
print(pairs)
"""[(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]"""


matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)
""""[[0, 1, 2], [0, 1, 2], [0, 1, 2]]"""


[expression for item in iterable if condition]
nums = [i for i in range(10) if i % 2 == 0]
print(nums)
"""[0, 2, 4, 6, 8]"""


for i in range(5):
    if i % 2 == 0:
        pass  # will do nothing
    else:
        print(i)

fruits = ["apple", "banana", "mango"]
for idx, fruit in enumerate(fruits):
    print(idx, fruit)

print(", ".join(str(i) for i in range(5) if i % 2 != 0))

"Questions "

val=[[i *j for i in range(1,4)] for j in range(1,5) ]
print(val)
"[[1, 2, 3], [2, 4, 6], [3, 6, 9], [4, 8, 12]]"





