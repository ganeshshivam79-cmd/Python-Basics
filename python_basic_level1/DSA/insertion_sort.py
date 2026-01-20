def insertion_sort(l1):
    for i in range(1, len(l1)):
        j = i - 1
        while j >= 0 and l1[j] > l1[j + 1]:
            l1[j], l1[j + 1] = l1[j + 1], l1[j]
            j -= 1
    return l1


print(insertion_sort([10,3,4,1,9,7,6,0,2]))

we will iterate and we will swap before element
like 1st to zero and 2nd to one and one to zero