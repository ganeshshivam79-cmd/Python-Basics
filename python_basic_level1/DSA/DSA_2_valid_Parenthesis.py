
def val(l1):
    stack=[]
    d1={"}":"{","]":"[",")":"("}
    for val in l1:
        if val not in d1:
            stack.append(val)
        else:
            if not stack:
                return False
            temp=stack.pop()
            if d1[val]!=temp:
                return False
    return True




l1="[{{[]}}])"

print(val(l1))