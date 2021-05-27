a = [7, 3, 4, 1, 5, 2]


def selection_sort(a):
    i = 0
    while i < len(a) - 1:
        iMin = i
        j = i + 1
        while j < len(a):
            if a[j] < a[iMin]:
                iMin = j
            j += 1
        if not i == iMin:
            a[i], a[iMin] = a[iMin], a[i]
        i += 1
    print("Selection sorted array: {}\n".format(a))


def insertion_sort(a):
    i = 1
    while i < len(a):

        j = i
        while j > 0 and a[j - 1] > a[j]:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1
        i += 1
    print("Insertion sorted array: {}\n".format(a))


def bubble_sort(a):
    i = 1
    while i < len(a):
        flag = 0
        j = 0
        while j < len(a) - i:
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                flag = True
            j += 1
        i += 1
        if not flag:
            break
    print("Bubble sorted array: {}\n".format(a))


def merge(a, first, mid, last):
    ll = mid - first + 1  # left length
    lr = last - mid  # right length
    l = [None] * ll
    r = [None] * lr
    i = 0
    while i < ll:
        l[i] = a[first + i]
        i += 1
    j = 0
    while j < lr:
        r[j] = a[mid + j + 1]
        j += 1
    i = 0
    j = 0
    k = first
    while i < ll and j < lr:
        if l[i] < r[j]:
            a[k] = l[i]
            i += 1
        else:
            a[k] = r[j]
            j += 1
        k += 1

    while i < ll:
        a[k] = l[i]
        i += 1
        k += 1
    while j < lr:
        a[k] = r[j]
        j += 1
        k += 1


def merge_sort(a, first, last):
    if first < last:
        mid = (first + last) // 2
        merge_sort(a, first, mid)
        merge_sort(a, mid + 1, last)
        merge(a, first, mid, last)


def quick_sort(a, first, last):
    if first < last:
        p = partition(a, first, last)
        quick_sort(a, first, p - 1)
        quick_sort(a, p + 1, last)


def partition(a, first, last):
    lastp1 = first
    first_unknown = first + 1
    while first_unknown <= last:
        if a[first_unknown] < a[first]:
            lastp1 += 1
            a[first_unknown], a[lastp1] = a[lastp1], a[first_unknown]
        first_unknown += 1
    a[first], a[lastp1] = a[lastp1], a[first]
    return lastp1


def heapify(a, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and a[largest] < a[l]:
        largest = l

    if r < n and a[largest] < a[r]:
        largest = r


    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, n, largest)


def heap_sort(a):
    hl = len(a)
    for i in range(hl // 2 - 1, -1, -1):
        heapify(a, hl, i)

    for i in range(hl - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heapify(a, i, 0)


selection_sort(a)
a = [7, 3, 4, 1, 5, 2]
bubble_sort(a)
a = [7, 3, 4, 1, 5, 2]
insertion_sort(a)
a = [7, 3, 4, 1, 5, 2]
merge_sort(a, 0, len(a) - 1)
print("Merge sorted array: {}\n".format(a))
a = [7, 3, 4, 1, 5, 2]
quick_sort(a, 0, len(a) - 1)
print("Quick sorted array: {}\n".format(a))
a = [7, 3, 4, 1, 5, 2]
heap_sort(a)
print("Heap sorted array: {}\n".format(a))

