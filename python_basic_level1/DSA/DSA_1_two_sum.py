def val(l1, target):
    d1 = {}
    for i in range(len(l1)):
        diff = target - l1[i]
        if diff in d1:
            return [d1[diff], i]
        d1[l1[i]] = i
    return None


l1 = [5, 6, 8, 9, 1, 10]
target = 20
print(val(l1, target))