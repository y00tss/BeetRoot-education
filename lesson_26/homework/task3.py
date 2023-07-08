import random
import time

def quicksort(arr, partition_limit):
    if len(arr) <= partition_limit:
        insertionSort(arr)
        return arr

    _quicksort(arr, 0, len(arr) - 1, partition_limit)
    return arr


def _quicksort(arr, low, high, partition_limit):
    if low < high:
        if high - low <= partition_limit:
            insertionSortRange(arr, low, high)
        else:
            pivot_idx = partition(arr, low, high)
            _quicksort(arr, low, pivot_idx - 1, partition_limit)
            _quicksort(arr, pivot_idx + 1, high, partition_limit)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def insertionSortRange(arr, low, high):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


list_size = 10_000
random_list = [random.randint(1, list_size) for _ in range(list_size)]

partition_limits = [10, 50, 100, 500, 1000, 5000, 10000]

for limit in partition_limits:
    start_time = time.time()
    sorted_list = quicksort(random_list.copy(), limit)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Partition Limit: {limit}\tExecution Time: {execution_time} seconds")
