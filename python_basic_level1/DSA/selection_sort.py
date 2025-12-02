def selection_sort(l1):
    min_index = 0
    for i in range(0, len(l1) - 1):
        for j in range(i + 1, len(l1)):
            if l1[min_index] > l1[j]:
                min_index = j
        if l1[min_index] < l1[i]:
            l1[min_index], l1[i] = l1[i], l1[min_index]
    return l1


print(selection_sort([10, 9, 8, 2, 3, 4, 1, 0]))


