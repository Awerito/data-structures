import random as rnd
import time as t

def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1

        while low <= high and array[low] <= pivot:
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high

def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)

#Test
s = []
for i in range(10001):
	s.append(rnd.randint(1, 100))

t0 = t.time()
quick_sort(s, 0, len(s) - 1)
t1 = t.time()

print(t1 - t0)
# 0.06415557861328125
