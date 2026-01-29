d1=dict()
d1[10]=d1.get("ke",0)
print(d1)
print(set(d1))

d2={"k1":12,"k2":20}
print(set(d1)  |set(d2))  # Union
d2.setdefault("k3",20)
print(d2)
d2=dict(sorted(d2.items(), key=lambda x:x[1]))
print(d2)     # ascending
val=map(lambda x:x**2,d2.values())
d5=dict(zip(d2.keys(),val))   #map the values
print(d5)

d3=dict.fromkeys([20,30],1)
print(d3)    #create a default dictionary


d1 = defaultdict(lambda: 30)
print(d.setdefault("a", 0))


d1={"a":[10,3,45],"b":[34,5,67]}
d2={k:v for k,v in d1.items() if v[1]%2==0}
print(d2)


### reverse them
d = {"a": 1, "b": 2}
rev = {v: k for k, v in d.items()}
print(rev)