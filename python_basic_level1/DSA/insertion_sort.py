def insertion_sort(l1):
    for i in range(0,len(l1)):
        j=i-1
        for m in range(0,i):
            if j>=0 and l1[j+1]<l1[j]:
                l1[j+1],l1[j]=l1[j],l1[j+1]
                j=j-1
    return l1

print(insertion_sort([10,3,4,1,9,7,6,0,2]))

we will iterate and we will swap before element
like 1st to zero and 2nd to one and one to zero