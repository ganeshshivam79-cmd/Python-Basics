def sell_stock(l1):
    l, r = 0, 1
    max_value = 0
    while r < len(l1):
        if l1[l] < l1[r]:
            val = l1[r] - l1[l]
            max_value = max(val, max_value)
        else:
            l = r
        r += 1
    return max_value


print(sell_stock([10, 9, 4, 5, 1, 3, 22]))

when r less than l swap it . if not check for max in them easy one