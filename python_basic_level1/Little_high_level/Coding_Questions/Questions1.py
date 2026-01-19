
"""sort by second element"""
l1 = [(10,2),(11,1),(6,0),(9,3)]
val = list(map(lambda x: x[1], l1))
print(val)

"""" or value """
l1.sort(key=lambda x: x[1])
print(l1)
[(6, 0), (11, 1), (10, 2), (9, 3)]


str1 = ["val pi", "sec mk"]
str1.sort(key=lambda x: x.split()[1])
print(str1)
str1 = ["val pi", "sec mk"]

nums = ["".join(filter(str.isdigit, s)) for s in l]