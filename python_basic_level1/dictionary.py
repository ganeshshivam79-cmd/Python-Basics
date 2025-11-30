




from collections import defaultdict
c = defaultdict(lambda: 5)
print(c['apple'])   # 5


d = dict.fromkeys(["a", "b", "c"], 0)
print(d)   # {'a': 0, 'b': 0, 'c': 0}
