#merge sort
l1 = [23, 23, 4, 54, 3, 2, 4, 5, 455, 34, 534, 53, 4, 34, 34, 53, ]


def merge_Sort(l1):
    if len(l1) <= 1:
        return l1
    midpoint = len(l1)//2
    #print(midpoint)
    leftside = l1[:midpoint]
    rightside = l1[midpoint:]
    #print(leftside)
    #print(rightside)
    left1 = merge_Sort(leftside)
    right1 = merge_Sort(rightside)
    return merging(left1,right1)


def merging(l1,l2):
    result = []
    i = j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1

    result.extend(l1[i:])
    result.extend((l2[j:]))

    return result


a = merge_Sort(l1)
print(a)

#Reverse Merge Sort
l1 = [3, 4, 55, 3, 2, 4, 5, 9, 43]


def merge_sort(l1):
    if len(l1) <= 1:
        return l1
    midpoint = len(l1)//2
    leftside = l1[:midpoint]
    #print(leftside)
    rightside = l1[midpoint:]
    #print(rightside)
    #print(midpoint)
    left1 = merge_sort(leftside)
    right1 = merge_sort(rightside)
    return merging(left1,right1)


def merging(l1,l2):
    result = []
    i = j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] > l2[j]:
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1

    result.extend(l1[i:])
    result.extend(l2[j:])

    return result


a = merge_sort(l1)
print(a)

#merge sort with for loop
l1 = [3, 4, 55, 3, 2, 4, 5, 45, 21, 89, 9, 43]


def merge_Sort(l1):
    if len(l1) <= 1:
        return l1
    midpoint = len(l1)// 2
    #print(midpoint)
    leftside = l1[:midpoint]
    rightside = l1[midpoint:]
    #print(leftside)
    #print(rightside)
    left1 = merge_Sort(leftside)
    right1 = merge_Sort(rightside)
    return merging(left1, right1)


def merging(l1, l2):
    result = []
    i = j = 0
    total_length = len(l1) + len(l2)
    for xyz in range(total_length):
        if i < len(l1) and (j >= len(l2) or l1[i] < l2[j]):
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1

    return result


a = merge_Sort(l1)
print(a)