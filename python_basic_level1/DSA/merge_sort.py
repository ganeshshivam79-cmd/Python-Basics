def merge(l1, l2):
    combined = []
    i, j = 0, 0

    while i < len(l1) and j < len(l2):
        if l1[i] > l2[j]:
            combined.append(l2[j])
            j += 1
        elif l1[i] < l2[j]:
            combined.append(l1[i])
            i += 1

    while i < len(l1):
        combined.append(l1[i])
        i += 1

    while j < len(l2):
        combined.append(l2[j])
        j += 1
    return combined


def merge_sort(val):
    if len(val) == 1:
        return val

    left = merge_sort(val[0:(len(val)) // 2])
    right = merge_sort(val[(len(val)) // 2:len(val)])

    return merge(left, right)


print(merge_sort([10, 2, 3, 4, 9]))


