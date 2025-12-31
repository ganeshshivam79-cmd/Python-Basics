
from collections import defaultdict
c = defaultdict(lambda: 5)
print(c['apple'])   # 5


d = dict.fromkeys(["a", "b", "c"], 0)
print(d)   # {'a': 0, 'b': 0, 'c': 0}


dict1=dict()
dict1["a"]=[[10,2]]
print(dict1["a"][0][1])
dict1["a"].append([56])
print(dict1)