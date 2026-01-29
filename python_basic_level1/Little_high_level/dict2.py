new_d = { (v if v > 10 else k): (k if v > 10 else v)
          for k, v in d.items() }
#swap needed at neded specific condition

d = {"a": 5, "b": 15, "c": 10}

#for key swap and condition
d = {v + 10 if v > 10 else v: k for k, v in d.items()}
print(d)

#for value  condition
d = {k.upper(): v if v<10 else v+10 for k, v in d.items()}
print(d)