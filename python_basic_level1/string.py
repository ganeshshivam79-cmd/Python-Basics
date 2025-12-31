.upper(), .lower(), .title(), .capitalize()

.strip(), .lstrip(), .rstrip()

.split(), .join()

.replace(old, new)

.find(), .index(), .count()

.startswith(), .endswith()

",".join(map(str, d.values()))  # '1,2'

l1=[2,3,4]
v1=[str(x) for x in l1]
print(v1)
val=''.join(map(str,l1))
print(val)