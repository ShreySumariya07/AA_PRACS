import time
import random
import sys
import copy

sys.setrecursionlimit(10**9)


def partiton(low, high, arr):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


def quicksort(low, high, arr):
    if low <= high:
        pi = partiton(low, high, arr)
        quicksort(low, pi-1, arr)
        quicksort(pi+1, high, arr)


def randpartition(low, high, arr):
    randpivot = random.randrange(low, high)
    arr[high], arr[randpivot] = arr[randpivot], arr[high]
    return partiton(low, high, arr)


def randquicksort(low, high, arr):
    if low <= high:
        pi = randpartition(low, high, arr)
        quicksort(low, pi-1, arr)
        quicksort(pi+1, high, arr)


iterations = int(input("Enter the number of iterations:"))
for i in range(iterations):
    arr = []
    n = int(input("Enter the number of elements:"))
    for i in range(n):
        arr.append(random.randint(1, n))

    arr2 = copy.deepcopy(arr)
    quick1 = time.time()
    quicksort(0, n-1, arr)
    # print(arr)
    quick2 = time.time()
    print("Time for Quick Sort for", (i+1), "elements:", quick2-quick1)

    randquick1 = time.time()
    randquicksort(0, n-1, arr2)
    randquick2 = time.time()
    # print(arr)
    print("Time for randomized quick sort for ",
          (i+1), " elements", randquick2-randquick1)
