def selection_sort(l1):
    for i in range(len(l1) - 1):
        min_index = i   # ✅ reset for every pass

        for j in range(i + 1, len(l1)):
            if l1[j] < l1[min_index]:
                min_index = j

        l1[i], l1[min_index] = l1[min_index], l1[i]

    return l1

"""
find the min index and swap and with others and in end swap with main element
"""
