#bubble sort

a = [10, 8, 6, 2]


def bubble_sort(a):
    endindex = len(a)
    for i in range(0, endindex):
        #print(a[i])
        for j in range(0, endindex - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


d = bubble_sort(a)
print(d)
#time complexity = O(n)*2
#space complexity = O(1)

#Reverse Bubble Sort
a = [10, 8, 6, 2]


def bubble_sort(a):
    endindex = len(a)
    for i in range(0, endindex):
        #print(a[i])
        for j in range(0, endindex - i - 1):
            if a[j] < a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


d = bubble_sort(a)
print(d)