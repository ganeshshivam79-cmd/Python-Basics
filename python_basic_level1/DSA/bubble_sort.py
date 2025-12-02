def bubble_sort(l1):
    count = 1

    while count != 0:
        count = 0
        for i in range(len(l1) - 1):
            if l1[i] > l1[i + 1]:
                l1[i], l1[i + 1] = l1[i + 1], l1[i]
                count = 1
    return l1


print(bubble_sort([10, 3, 4, 1, 9, 7, 6, 0, 2]))

#looping through them and swapping two values , then swapping two by randomly moving