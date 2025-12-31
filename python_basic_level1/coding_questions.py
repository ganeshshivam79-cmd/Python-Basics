v1=[1,2,3]
v2=''.join(str(i) for i in v1)
print(v2)

v1 = [i if i % 2 != 0 else -1 for i in range(1, 10)]
print(v1)

nums = [1, 2, 3, 4]
odd = list(filter(lambda x: x % 2 != 0, nums))
print(odd)